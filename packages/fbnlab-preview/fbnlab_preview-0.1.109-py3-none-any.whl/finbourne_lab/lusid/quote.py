from finbourne_lab.lusid.base import BaseLusidLab
from finbourne_lab.lusid import LusidExperiment
from finbourne_lab.lusid.ensure import QuotesData, InstrumentData
import shortuuid


class LusidQuoteLab(BaseLusidLab):
    """Lab class for lusid qutes endpoint methods.

    """
    quotes_data = QuotesData(quiet=False)
    instrument_data = InstrumentData(quiet=False)

    def upsert_quotes_measurement(self, **kwargs) -> LusidExperiment:
        """Make an experiment object for lusid upsert quotes' performance.

        Keyword Args:
            x_rng (Union[int, List[int]]): the range to sample when upserting x-many quotes. Given as a list
                containing two integers or a const int value. Defaults to [1, 2000].
            scope: scope of the quotes, defaults to f"fbnlab-test-{str(shortuuid.uuid())}"
            id_prefix: prefix for naming the instruments, defaults to "fbnlab-test-instruments"

        Returns:
            LusidExperiment: the upsert quotes experiment object.
        """

        x_rng = kwargs.get('x_rng', [1, 2000])
        scope = kwargs.get('scope', f"fbnlab-test-{str(shortuuid.uuid())}")
        id_prefix = "fbnlab-test-inst-for-quotes"

        self.instrument_data.ensure(n_insts=x_rng[1], id_prefix=id_prefix)

        method = self.lusid.quotes_api.upsert_quotes

        def build(x):
            instrument_ids = [f"{id_prefix}_{i}" for i in range(x)]
            quote_ids = [self.quotes_data.build_quote_id(instrument_id) for instrument_id in instrument_ids]
            request_key_pairs = self.quotes_data.build_upsert_quote_request_key_pairs(quote_ids)
            return lambda: method(scope, request_body=request_key_pairs, _preload_content=False)

        return LusidExperiment('upsert_quotes', build, x_rng)

    def get_quotes_measurement(self, **kwargs) -> LusidExperiment:
        """Make an experiment object for lusid get quotes' performance.

        Keyword Args:
            x_rng (Union[int, List[int]]): the range to sample when getting x-many quotes. Given as a list
                containing two integers or a const int value. Defaults to [1, 2000].
            scope: scope of the quotes, defaults to f"fbnlab-test-{str(shortuuid.uuid())}"
            id_prefix: prefix for naming the instruments, defaults to "fbnlab-test-instruments"

        Returns:
            LusidExperiment: the get quotes experiment object.
        """

        x_rng = kwargs.get('x_rng', [1, 2000])
        scope = kwargs.get('scope', f"fbnlab-test-{str(shortuuid.uuid())}")
        id_prefix = "fbnlab-test-instruments"

        self.instrument_data.ensure(n_insts=x_rng[1], id_prefix=id_prefix)
        instrument_ids = [f"{id_prefix}_{i}" for i in range(x_rng[1])]
        quote_series_ids = [self.quotes_data.build_quote_series_id(instrument_id) for instrument_id in instrument_ids]
        keys = [f"quotes_{i}" for i in range(len(quote_series_ids))]
        quote_key_pairs = dict(zip(keys, quote_series_ids))
        self.quotes_data.ensure(
            scope=scope,
            instrument_ids=instrument_ids,
            quote_key_pairs=quote_key_pairs)

        method = self.lusid.quotes_api.get_quotes

        def build(x):
            _instrument_ids = [f"{id_prefix}_{i}" for i in range(x)]
            _quote_series_ids = [
                self.quotes_data.build_quote_series_id(_instrument_id)
                for _instrument_id in _instrument_ids]
            _keys = [f"quotes_{i}" for i in range(len(_quote_series_ids))]
            _quote_key_pairs = dict(zip(_keys, _quote_series_ids))
            return lambda: method(scope, request_body=_quote_key_pairs, _preload_content=False)

        return LusidExperiment('get_quotes', build, x_rng)