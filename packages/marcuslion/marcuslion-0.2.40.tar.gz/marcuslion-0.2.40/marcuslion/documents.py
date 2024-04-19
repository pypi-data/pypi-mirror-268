import io
import urllib
import urllib3

import pandas as pd

from marcuslion.config import base_url, api_key, api_version
from marcuslion.restcontroller import RestController


class Documents(RestController):
    """
    MarcusLion Documents class
    """

    def __init__(self):
        super().__init__(api_version + "/documents")

    def list(self) -> pd.DataFrame:
        """
        Documents.list()
        """
        return super().verify_get_data("", {})

    def search(self, search, provider_list) -> pd.DataFrame:
        """
        Documents.search(search)
        """
        params = {"providers": provider_list, "title": search}
        return super().verify_get_data("search", params)

    def query(self, ref):
        """
        Documents.query(ref)
        """
        pass

    def download(self, ref) -> pd.DataFrame:
        """
        Documents.download(ref)
        """
        pass
