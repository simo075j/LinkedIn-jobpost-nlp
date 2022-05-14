import numpy as np
import pandas as pd
import yfinance
import io
from datetime import date
from azure.storage.blob import *

class yftocsv(object):
    def __init__(self, ticker):
        self.ticker = ticker
        
    def apitocsv(self):
        data = yfinance.Ticker(self.ticker).history(period='max')
        data.info()
        output = data.to_csv(encoding='utf-8')

class csvtoblob(object):
    def __init__(self, ticker):
        self.ticker = ticker

    def writeToBlob(self):
        blob_block = ContainerClient.from_connection_string(
            conn_str= "DefaultEndpointsProtocol=https;AccountName=yfinancedl;AccountKey=np3883RQuFec82DvT1yUOD1qUw4KuMl4+AQ4Hk2AeC9doyjsmz778gEDTJoFVKK8XtCKTbhJoZxCtQ3A7kxqxg==;EndpointSuffix=core.windows.net",
            container_name= "tickerinfo"
            )
        output = io.StringIO()
        name = f"{self.ticker}.csv"
        blob_block.upload_blob(name, output, overwrite=True, encoding='utf-8')

#yftocsv.apitocsv(input('GME'))

gme = yftocsv("gme").apitocsv()
#apitocsv("GME")
#writeToBlob(apitocsv("GME"),"GME")
