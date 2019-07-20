import pandas as pd 
import requests
import pdb

#url = 'https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=1416'

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

pdb.set_trace()

