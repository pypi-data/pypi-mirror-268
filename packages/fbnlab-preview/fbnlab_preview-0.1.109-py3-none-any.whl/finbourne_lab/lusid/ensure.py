from finbourne_lab.lusid.client import LusidClient
from finbourne_lab.common.ensure import BaseData
from lusid.exceptions import ApiException
from lusid import PropertyValue
import lusid.models as models
from urllib3.response import HTTPResponse
from lumipy.common import indent_str
from typing import Union, List
from lumipy import get_client
from datetime import datetime
import pytz
import numpy as np
import os
import shortuuid
import numpy as np


class BaseLusidData(BaseData):
    """Base class for lusid data ensure steps.

    You are required to implement the ensure and check_data methods.
    """

    def __init__(self, quiet: bool):
        """The constructor of the base lusid data class.

        Args:
            quiet (bool): whether to switch off log messages.
        """
        lm_client = get_client()
        client = LusidClient(token=lm_client.get_token(), api_url=os.environ['FBN_LUSID_API_URL'])
        self.client = client
        super().__init__(quiet)

    def check_data(self, **kwargs):
        pass

    def write_data(self, **kwargs) -> Union[List[HTTPResponse], ApiException, bool]:
        pass

    def ensure(self, **kwargs):
        self.log(f'Checking data {kwargs}')
        if self.check_data(**kwargs):
            self.log('Data are present. Ready to go!')
            return True

        self.log('Data not ready. Writing...')
        response = self.write_data(**kwargs)
        if isinstance(response, List):
            for r in response:
                if isinstance(r, HTTPResponse):
                    response_data = r.json()
                    if response_data.get('failed'):
                        failed_type = response_data['failed'][0]['type']
                        failed_detail = response_data['failed'][0]['detail']
                        failed_error_details = response_data['failed'][0]['errorDetails']
                        err_msgs = f"{failed_type}\n{failed_detail}\n{failed_error_details}"
                        raise ValueError(f'Write failed!\n{indent_str(err_msgs)}')
        elif isinstance(response, ApiException):
            raise ValueError(f'Write failed!\n{indent_str(str(response))}')

        self.log('Data written. Ready to go!')
        return response


class PortfolioData(BaseLusidData):

    def check_data(self, scope, portfolio_codes, effective_date):

        for portfolio_code in portfolio_codes:
            try:
                self.client.portfolios_api.get_portfolio(scope=scope, code=portfolio_code)
            except ApiException as e:
                return False
        return True

    def write_data(self, scope, portfolio_codes, effective_date):
        responses = []
        for portfolio_code in portfolio_codes:
            try:
                self.client.portfolios_api.get_portfolio(scope=scope, code=portfolio_code)
            except ApiException as e:
                transactions_portfolio_request = models.CreateTransactionPortfolioRequest(
                    display_name="test portfolio",
                    code=portfolio_code,
                    base_currency="GBP",
                    created=effective_date
                )
                responses.append(self.client.transaction_portfolios_api.create_portfolio(
                    scope=scope,
                    create_transaction_portfolio_request=transactions_portfolio_request
                ))
        return responses

    def ensure(self, scope, portfolio_codes, effective_date):
        return super().ensure(
            scope=scope,
            portfolio_codes=portfolio_codes,
            effective_date=effective_date)

    @staticmethod
    def build_portfolio_codes(n_portfolios, code_prefix):
        return [f"portfolio-{code_prefix}-{i}" for i in range(n_portfolios)]


class InstrumentData(BaseLusidData):

    def check_data(self, n_insts, id_prefix, scope="default", properties=None):

        property_keys = []
        if properties is not None:
            property_keys = [prop.key for prop in properties]
        identifiers = [f"{id_prefix}_{i}" for i in range(n_insts)]
        instrument_api = self.client.instruments_api
        response = instrument_api.get_instruments(
            identifier_type="ClientInternal",
            request_body=identifiers,
            scope=scope,
            property_keys=property_keys,
            _preload_content=False
        )
        response_data = response.json()
        # (not response_data['failed']) will be True if data present and there was no failure
        return not response_data['failed']

    def write_data(self, n_insts, id_prefix, scope="default", properties=None):

        instruments = {
            f'inst_{i}': models.InstrumentDefinition(
                name=f'Instrument{i}',
                identifiers={"ClientInternal": models.InstrumentIdValue(f'{id_prefix}_{i}')},
                properties=properties
            )
            for i in range(n_insts)
        }

        return [self.client.instruments_api.upsert_instruments(
            request_body=instruments,
            scope=scope,
            _preload_content=False)]

    def ensure(self, n_insts, id_prefix, scope="default", properties=None):
        return super().ensure(
            n_insts=n_insts,
            id_prefix=id_prefix,
            scope=scope,
            properties=properties
        )


class HoldingsData(BaseLusidData):

    def check_data(self, n_holdings, scope, code_prefix, portfolio_code, instrument_identifiers, property_keys=None):
        if property_keys is None:
            property_keys = {}
        try:
            self.client.transaction_portfolios_api.get_holdings(
                scope=scope,
                code=portfolio_code,
                property_keys=property_keys,
                _preload_content=False)
        except ApiException as e:
            return False

        return True

    def write_data(self, n_holdings, scope, code_prefix, portfolio_code, instrument_identifiers, property_keys=None):

        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        adjust_holding_request = HoldingsData.build_holdings_adjustments_request(
            n_holdings=n_holdings,
            instrument_identifiers=instrument_identifiers,
            property_keys=property_keys
        )

        return [self.client.transaction_portfolios_api.set_holdings(
            scope=scope,
            code=portfolio_code,
            adjust_holding_request=adjust_holding_request,
            effective_at=effective_date,
            _preload_content=False)
        ]

    def ensure(self, n_holdings, scope, code_prefix, portfolio_code, instrument_identifiers, property_keys=None):
        return super().ensure(
            n_holdings=n_holdings,
            scope=scope,
            code_prefix=code_prefix,
            portfolio_code=portfolio_code,
            instrument_identifiers=instrument_identifiers,
            property_keys=property_keys
        )

    @staticmethod
    def build_holdings_adjustments_request(n_holdings, instrument_identifiers, property_keys=None):
        if property_keys is None:
            property_keys = []
        return [models.AdjustHoldingRequest(
            instrument_identifiers=instrument_identifiers[i],
            properties=property_keys,
            tax_lots=[models.TargetTaxLotRequest(units=100.00,
                                                 price=101.00,
                                                 cost=models.CurrencyAndAmount(amount=10100.0, currency="GBP"),
                                                 portfolio_cost=10100.0)]
        ) for i in range(n_holdings)]


class TxnsData(BaseLusidData):

    def check_data(self, n_txns, scope, code_prefix, portfolio_code, instrument_identifiers, property_keys=None):
        if property_keys is None:
            property_keys = {}
        try:
            self.client.transaction_portfolios_api.get_transactions(
                scope=scope,
                code=portfolio_code,
                property_keys=property_keys,
                _preload_content=False)
        except ApiException as e:
            return False

        return True

    def write_data(self, n_txns, scope, code_prefix, portfolio_code, instrument_identifiers, property_keys=None):

        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        transactions = TxnsData.build_transactions(
            n_transactions=n_txns,
            instrument_identifiers=instrument_identifiers,
            effective_date=effective_date,
            properties=property_keys)

        return [self.client.transaction_portfolios_api.upsert_transactions(
            scope=scope,
            code=portfolio_code,
            transaction_request=transactions,
            _preload_content=False)
        ]

    def ensure(self, n_txns, scope, code_prefix, portfolio_code, instrument_identifiers, property_keys=None):
        return super().ensure(
            n_txns=n_txns,
            scope=scope,
            portfolio_code=portfolio_code,
            code_prefix=code_prefix,
            instrument_identifiers=instrument_identifiers,
            property_keys=property_keys
        )

    @staticmethod
    def build_transactions(n_transactions, instrument_identifiers, effective_date, properties=None):

        if properties is None:
            properties = {}

        return [models.TransactionRequest(
            transaction_id=str(shortuuid.uuid()),
            # transaction type, configured during system setup
            type="Buy",
            instrument_identifiers=instrument_identifiers,
            transaction_date=effective_date.strftime("%Y-%m-%d"),
            settlement_date=effective_date.strftime("%Y-%m-%d"),
            units=100,
            transaction_price=models.TransactionPrice(12.3),
            total_consideration=models.CurrencyAndAmount(1230, "GBP"),
            source="default",
            properties=properties,
            transaction_currency="GBP"
        ) for _ in range(n_transactions)]


class PropertiesData(BaseLusidData):

    def check_data(self, n_props, scope, domain):

        for i in range(n_props):
            try:
                self.client.property_defs_api.get_property_definition(
                    domain=domain,
                    scope=scope,
                    code=f"test_prop{i}"
                )
            except ApiException as e:
                return False
        return True

    def write_data(self, n_props, scope, domain):
        """ Build a number of property objects for a certain scope and domain.

                Args:
                    n_props: number of properties to build
                    scope: scope where the properties wil be created
                    domain: domain of the entity the properties belong to

                Returns:
                """

        responses = []

        for i in range(n_props):
            try:
                property_definition = models.CreatePropertyDefinitionRequest(
                    domain=domain,
                    scope=scope,
                    life_time="Perpetual",
                    code=f"test_prop{i}",
                    value_required=False,
                    data_type_id=models.ResourceId("system", "number"),
                    display_name="test_property"
                )
                # create the property
                responses.append(self.client.property_defs_api.create_property_definition(
                    create_property_definition_request=property_definition))
            except ApiException as e:
                return e

        return responses

    def ensure(self, n_props, scope, domain):
        return super().ensure(n_props=n_props, scope=scope, domain=domain)

    @staticmethod
    def build_properties(n_props, scope, domain):


        properties = [
            models.ModelProperty(
                key=f'{domain}/{scope}/test_prop{i}',
                value=PropertyValue(metric_value=models.MetricValue(value=i * 100))
            )
            for i in range(n_props)
        ]
        return properties

    @staticmethod
    def build_perpetual_properties(n_props, scope, domain):

        properties = [
            models.PerpetualProperty(
                key=f'{domain}/{scope}/test_prop{i}',
                value=PropertyValue(metric_value=models.MetricValue(value=i * 100))
            )
            for i in range(n_props)
        ]
        return properties


class QuotesData(BaseLusidData):

    def check_data(self, scope, instrument_ids, quote_key_pairs):
        try:
            response = self.client.quotes_api.get_quotes(
                scope=scope,
                request_body=quote_key_pairs,
                _preload_content=False
            )
        except ApiException as e:
            return False
        response_data = response.json()
        if response_data['notFound']:
            return False
        return True

    def write_data(self, scope, instrument_ids, quote_key_pairs):
        quote_ids = [QuotesData.build_quote_id(instrument_id) for instrument_id in instrument_ids]
        request_key_pairs = self.build_upsert_quote_request_key_pairs(quote_ids)
        response = self.client.quotes_api.upsert_quotes(
            scope=scope,
            request_body=request_key_pairs,
            _preload_content=False
        )
        return [response]

    def ensure(self, scope, instrument_ids, quote_key_pairs):
        return super().ensure(scope=scope, instrument_ids=instrument_ids, quote_key_pairs=quote_key_pairs)

    @staticmethod
    def build_upsert_quote_request_key_pairs(quote_ids):

        requests = [models.UpsertQuoteRequest(
            quote_id=quote_id,
            metric_value=models.MetricValue(
                value=np.random.randint(200),
                unit="USD"
            )
        ) for quote_id in quote_ids]

        # keys to be used to create the dict that will become our request body
        keys = [f"quotes_{i}" for i in range(len(requests))]

        return dict(zip(keys, requests))

    @staticmethod
    def build_quote_id(instrument_id):
        return models.QuoteId(
                QuotesData.build_quote_series_id(instrument_id),
                effective_at=datetime(2019, 4, 15, tzinfo=pytz.utc).strftime("%Y-%m-%d")
            )

    @staticmethod
    def build_quote_series_id(instrument_id):
        return models.QuoteSeriesId(
                    provider="DataScope",
                    instrument_id=instrument_id,
                    instrument_id_type="Figi",
                    quote_type="Price",
                    field="mid"
                )