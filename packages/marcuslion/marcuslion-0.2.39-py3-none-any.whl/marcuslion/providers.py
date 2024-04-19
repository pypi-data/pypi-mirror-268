import pandas as pd

from marcuslion.config import api_version
from marcuslion.restcontroller import RestController


class Providers(RestController):
    """
    MarcusLion Providers class
    $ curl 'https://qa1.marcuslion.com/core/datasets/providers'
    """

    def __init__(self):
        super().__init__(api_version + "/datasets/providers")

    def list(self) -> pd.DataFrame:
        """
        Providers.list()
        """
        return super().verify_get("", {})

    # def search(self, search) -> pd.DataFrame:
    #     """
    #     Providers.search(search)
    #     """
    #     params = {"search": search}
    #     return super().verify_get("search",  params)

    def query(self, uid) -> pd.DataFrame:
        """
        Providers.query()
        """
        params = {"id": uid}
        return super().verify_get("",  params)


