import pandas as pd

from marcuslion.DataGatewayInterface import DataGatewayInterface
from marcuslion.config import api_version
from marcuslion.restcontroller import RestController


class UsSec(DataGatewayInterface):
    """
    MarcusLion UsSec
        https://qa1.marcuslion.com/swagger-ui/index.html#/sec-controller
    """
    def __init__(self):
        super().__init__(api_version + "/us-sec-edgar/company-facts")

    def list(self) -> pd.DataFrame:
        return super().verify_get_df()

    def query(self, cik) -> pd.DataFrame:
        return super().verify_get_df(f"{cik}")

    def get_fields(self, cik) -> any:
        return super().verify_get(f"{cik}")

    def get_units(self, cik, field) -> pd.DataFrame:
        return super().verify_get(f"{cik}/{field}")

    def search(self, search, provider_list) -> pd.DataFrame:
        # params = {"providers": provider_list, "title": search}
        # return super().verify_get_data("search", params)
        pass

    def download(self, cik) -> pd.DataFrame:
        pass
