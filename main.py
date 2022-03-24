import numpy as np
import pandas as pd
import yfinance
import io
from datetime import date
from azure.storage.blob import *

def apitocsv(ticker):
    data = yfinance.Ticker("GME").history(period='max')
    data.info()


def writeToBlob(file):
    blob_block = ContainerClient.from_connection_string(
        conn_str= "DefaultEndpointsProtocol=https;AccountName=yfinancedl;AccountKey=np3883RQuFec82DvT1yUOD1qUw4KuMl4+AQ4Hk2AeC9doyjsmz778gEDTJoFVKK8XtCKTbhJoZxCtQ3A7kxqxg==;EndpointSuffix=core.windows.net",
        container_name= "tickerinfo"
        )
    output = io.StringIO()
    output = data.to_csv(encoding='utf-8')
    name = "gme.csv"
    blob_block.upload_blob(name, output, overwrite=True, encoding='utf-8')