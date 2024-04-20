import io
import urllib
import urllib3

import pandas
from marcuslion.config import api_version
from marcuslion.restcontroller import RestController


class TimeSeries(RestController):
    """
    https://qa1.marcuslion.com/swagger-ui/index.html#/time-series-api-controller
    """

    def __init__(self):
        super().__init__(api_version + "/timeseries/")

    def list(self) -> pandas.DataFrame:
        """
        Indicators.list()
        """
        return super().verify_get()

    def list(self, symbol, interval, page_size) -> pandas.DataFrame:
        """
        Indicators.list()
        """
        return super().verify_get(symbol + "/" + interval + "/" + str(page_size), {})

    def query(self, ref):
        return super().verify_get_data("query", {"ref", ref})

    def search(self, search) -> pandas.DataFrame:
        return super().verify_get_data("search", {"search", search})

    def candles(self, params) -> pandas.DataFrame:
        """
        TimeSeries.candles(ref, params)
        """
        res = super().verify_get("history", params)
        if res is None or 'data' not in res:
            return pandas.DataFrame()

        df = pandas.DataFrame(res['data'], columns=res['schema'])
        df.name = res['entityKey']['symbol'] + "_" + res['interval']
        df["timestamp"] = pandas.to_datetime(df["timestamp"], unit='ms')
        return df

    def trades(self, params) -> pandas.DataFrame:
        """
        TimeSeries.trades(ref, params)
        """
        res = super().verify_get("history/raw", params)
        if res is None or 'data' not in res:
            return pandas.DataFrame()

        df = pandas.DataFrame(res['data'], columns=res['schema'])
        df.name = res['entityKey']['symbol'] + "_trades"
        df["timestamp"] = pandas.to_datetime(df["timestamp"], unit='ms')
        return df

    def download_stooq(self, params) -> pandas.DataFrame:
        """
        Download stooq data from timebase
        """
        res = super().verify_get("history/stooq", params)
        if res is None or 'data' not in res:
            return pandas.DataFrame()
        return pandas.DataFrame(res['data'], columns=res['schema'])

    def subscribe(self, ref, params):
        """
        TimeSeries.subscribe(ref, params)
        """
        pass
