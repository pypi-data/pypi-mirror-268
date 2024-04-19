import os
import pandas as pd

from marcuslion.config import api_version
from marcuslion.restcontroller import RestController


class Projects(RestController):
    """
    MarcusLion Projects class
        # $ curl 'https://qa1.marcuslion.com/core/projects'
    """

    def __init__(self, datasets):
        super().__init__(api_version + "/projects")
        self.datasets = datasets

    def list(self) -> pd.DataFrame:
        """
        Projects.list()
        """
        return super().verify_get_df("", {})

    def get_project_metadata(self, project_id: str) -> any:
        """
        Projects.get_project_metadata(id)
        """
        return super().verify_get(project_id)

    def __download_dataset_files(self, datasets: list, output_path: str = None) -> None:
        os.mkdir(output_path)

        # Download dataset files
        if datasets is None:
            return
        for dataset in datasets:
            try:
                self.datasets.download(dataset["source"], dataset["refId"], dataset["file"], output_path)
            except ValueError as e:
                print(f"Failed to download dataset file {dataset['file']} for {dataset['refId']}: {e}")

    def load_project(self, project_id):
        """
        Projects.load_project(id)
        """
        try:
            metadata = self.get_project_metadata(project_id)
            print(f"Loading project {metadata['projectName']}")
            datasets = list(metadata['datasets'])

            self.__download_dataset_files(datasets, "./datasets")
        except ValueError as e:
            print(f"Failed to load project {project_id}: {e}")
