import pandas as pd

from marcuslion.config import api_version
from marcuslion.restcontroller import RestController


class Indicators(RestController):
    """
    MarcusLion Indicators class
    """

    def __init__(self):
        super().__init__(api_version + "/indicators")

    def list(self) -> pd.DataFrame:
        """
        Indicators.list()
        """
        return super().verify_get_df("", {})

    def query(self, uuid):
        return super().verify_get(uuid)

    def search(self, search) -> pd.DataFrame:
        data = super().verify_get("search", {"query": search})  # {"query", search}
        return data

    def download(self, params) -> pd.DataFrame:
        """
        Indicators.download(params)
        """
        res = super().verify_get("download", params)
        if res is None or 'indicator' not in res or 'data' not in res['indicator']:
            return pd.DataFrame()
        return pd.DataFrame(res['indicator']['data'], columns=res['indicator']['schema'])

    def subscribe(self, params) -> pd.DataFrame:
        """
        Indicators.subscribe(params)
        """
        return super().verify_get("subscribe", params)

    def recently(self):
        """
        Indicators.recently
        """
        data = super().verify_get("recently")
        return data
