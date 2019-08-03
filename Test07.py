import pandas as pd 
import requests
from bs4 import BeautifulSoup
import lxml.etree
import pdb

#url = "http://finance.sina.com.cn/realstock/company/sh601138/nc.shtml"
url = "http://quote.eastmoney.com/sh601138.html"



response = requests.get(
                url,
                headers={
                    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
                }
                )
        
html = response.content
#html = str(html, 'utf-8')       
tables = pd.read_html(html)

pdb.set_trace()


