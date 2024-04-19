import pandas as pd

from marcuslion.config import api_version
from marcuslion.restcontroller import RestController


class DataFrames(RestController):
    """
    MarcusLion Datasets class
        https://qa1.marcuslion.com/swagger-ui/index.html#/data-frames-api-controller
    """

    def __init__(self):
        super().__init__(api_version + "/dataframes")

    def list(self) -> pd.DataFrame:
        return super().verify_get_data("", None)

    def search(self, search, provider_list) -> pd.DataFrame:
        params = {"providers": provider_list, "title": search}
        return super().verify_get_data("search", params)

    def query(self, _id) -> pd.DataFrame:
        return super().verify_get("metadata", {"id": _id})

    def download(self, _id) -> pd.DataFrame:
        return super().verify_get("download/" + _id, {})
