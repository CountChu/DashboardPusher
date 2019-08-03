import pandas as pd 
import requests
from bs4 import BeautifulSoup
import lxml.etree
import pdb


url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail?region=US&lang=en&symbol=NBEV"
url = "https://histock.tw/shstock/601138"

response = requests.get(
                url
                )
        
html = response.content
html = str(html, 'utf-8')       

pdb.set_trace()


