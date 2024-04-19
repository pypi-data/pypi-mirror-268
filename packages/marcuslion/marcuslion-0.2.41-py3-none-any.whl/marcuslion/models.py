import io
import urllib
import urllib3

import pandas as pd

from marcuslion.config import api_version
from marcuslion.restcontroller import RestController


class Models(RestController):
    """
    MarcusLion Indicators class
    """

    def __init__(self):
        super().__init__(api_version + "/models")

    def list(self) -> pd.DataFrame:
        """
        Indicators.list()
        """
        return super().verify_get_df("", {})

    def query(self, ref):
        return super().verify_get_data("query", {"ref", ref})

    def search(self, search) -> pd.DataFrame:
        return super().verify_get_data("search", {"search", search})

    def download(self, ref, params) -> pd.DataFrame:
        """
        Indicators.download(ref, params)
        """
        pass

    def subscribe(self, ref, params):
        """
        Indicators.subscribe(ref, params)
        """
        pass
