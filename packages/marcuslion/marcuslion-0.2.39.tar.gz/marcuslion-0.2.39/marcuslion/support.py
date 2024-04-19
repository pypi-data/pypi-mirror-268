import pandas as pd

from marcuslion.config import api_version
from marcuslion.restcontroller import RestController


class Support(RestController):
    """
    MarcusLion Datasets class
        https://qa1.marcuslion.com/swagger-ui/index.html#/data-frames-api-controller
    """

    def __init__(self):
        super().__init__(api_version + "/support")  # /api/v2

    def standard_candles(self) -> pd.DataFrame:
        return super().verify_get_df("standardCandles", {})
