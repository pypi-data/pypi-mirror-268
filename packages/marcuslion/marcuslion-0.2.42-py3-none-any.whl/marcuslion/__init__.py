import logging
import ssl
import skimage as ski
import os.path
import pandas as pd

from marcuslion.datasets import Datasets
from marcuslion.projects import Projects
from marcuslion.providers import Providers
from marcuslion.dataproviders import DataProviders
from marcuslion.documents import Documents
from marcuslion.indicators import Indicators
from marcuslion.timeseries import TimeSeries
from marcuslion.models import Models
from marcuslion.dataframes import DataFrames
from marcuslion.support import Support
from marcuslion.ussec import UsSec

providers = Providers()
data_providers = DataProviders()
datasets = Datasets()
dataframes = DataFrames()
documents = Documents()
indicators = Indicators()
timeseries = TimeSeries()
models = Models()
support = Support()
projects = Projects(datasets)
us_sec = UsSec()


logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

logger.info("Start marcuslion lib")

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 2000)

# resource_path = os.path.join(os.path.split(__file__)[0], "resources")
# image = ski.io.imread(resource_path + "/marcus_lion_logo.jpg")
# ski.io.imshow(image)

# this required downgrading requests library to urllib3-1.24.3 to avoid SSL cert error
ssl._create_default_https_context = ssl._create_unverified_context

print("MarcusLion lib loaded")


def help1():
    print("  ml.providers.list() or ml.datasets.search()")





