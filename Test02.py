import pandas as pd 
import requests
import pdb

#url = 'https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=1416'

url = "https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID=2408"

response = requests.get(
                url, 
                headers={
                    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
                }
            )
        
html = response.content
html = str(html, 'utf-8')        

tables = pd.read_html(html)



#
# Get name and date
#

table = tables[10]
name = table[0][0]
print('name = %s' % name)
date = table[3][0]
print('date = %s' % date)

#
# Get price
#

table = tables[9]
price = table[0][2]
print('price = %s' % price)

pdb.set_trace()   

print(tables)