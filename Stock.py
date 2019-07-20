#
# FILENAME.
#       Stock.py - Stock Module.
#
# FUNCTIONAL DESCRIPTION.
#       The module collects stock. 
#
# NOTICE.
#       Author: visualge@gmail.com (Count Chu)
#       Created on 2019/7/20
#

#
# Include standard packages.
#

import logging
import pdb

#
# Include specific packages.
#

import ssl
import pandas
import datetime
import requests
import pandas as pd

def getCurrenttTwStock(stockId):
    #ssl._create_default_https_context = ssl._create_unverified_context

    url = "https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID=%s" % stockId
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
    name = name.replace('\xa0', ' ')
    logging.info('name = %s' % name)
    date = table[3][0]
    logging.info('date = %s' % date)

    #
    # Get price
    #

    table = tables[9]
    price = table[0][2]
    logging.info('price = %s' % price)    
    
    return (name, date, price)
