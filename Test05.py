import pandas as pd 
import requests
from bs4 import BeautifulSoup
import lxml.etree
import pdb


url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail?region=US&lang=en&symbol=NBEV"

response = requests.get(
                url, 
                headers={
                    "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
                    "X-RapidAPI-Key": "19aba0c098msh10c7f3dca16e53bp16a60cjsn4f79f1ca9676"
                }
                
                
            )
        
html = response.content
html = str(html, 'utf-8')       

pdb.set_trace()


