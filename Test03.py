import pandas as pd 
import requests
from bs4 import BeautifulSoup
import pdb


url = "https://finance.yahoo.com/quote/601138.SS?p=601138.SS"

response = requests.get(
                url, 
                headers={
                    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
                }
            )
        
html = response.content
html = str(html, 'utf-8')   

tables = pd.read_html(html)
print(tables[0])
print(tables[1])     

soup = BeautifulSoup(html, 'html.parser')
name = soup.select('div > h1')[0].text
print(name)

#tables = pd.read_html(html)

pdb.set_trace()

