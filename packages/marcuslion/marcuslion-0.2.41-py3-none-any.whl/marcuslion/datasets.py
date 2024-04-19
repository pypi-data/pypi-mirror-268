import pandas as pd

from marcuslion.config import api_version
from marcuslion.restcontroller import RestController


class Datasets(RestController):
    """
    MarcusLion Datasets class
        # $ curl 'https://qa1.marcuslion.com/core/datasets/search?providers=kaggle,usgov&title=bike'
    """

    def __init__(self):
        super().__init__(api_version + "/datasets")

    def list(self) -> pd.DataFrame:
        """
        Datasets.list()
        """
        return super().verify_get_data("", {})

    def search(self, search, provider_list) -> pd.DataFrame:
        """
        Datasets.search()
        """
        params = {"providers": provider_list, "title": search}

        return super().verify_get_data("search", params)

    def query(self, title) -> pd.DataFrame:
        """
        Datasets.query(ref)
        """
        return super().verify_get_data("search", {"title": title})

    def download(self, source, ref, file_name, output_path=None) -> any:
        """
        Datasets.download(ref)
        """
        print(f"Downloading {file_name} from {source}/{ref}...")
        return super().download_file(source + "/download", {"ref": ref, "file": file_name}, output_path)
