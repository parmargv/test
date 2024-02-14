import requests
import bs4
import urllib.request
# import pandas as pd
# from pandas import ExcelWriter
from bs4 import BeautifulSoup
# from openpyxl import load_workbook
# import xlwings as xw
# import time
import urllib3
import re
import urllib.parse
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from datetime import datetime

url_lg = 'https://chartink.com/login'
url = 'https://chartink.com/screener/best-swing-trade-cash-breakout-by-gvparmar'
#url='https://chartink.com/screener/daily-ichimuko'
headers = {
    'user-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"

    }

#r = requests.get(url,{'headers':headers})
payload = {
    'email':'parmargv@yahoo.com',
    'password':'Gvp@chart123'
        }
with requests.session() as s:
    s.get(url_lg, data=payload)
    r = s.get(url)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
#ab = soup.find_all("table",class_="table table-striped scan_results_table dataTable.no-footer")



    #sauce = urllib.request.urlopen('https://chartink.com/screener/best-swing-trade-cash-breakout-by-gvparmar')
    #soup  =bs4.BeautifulSoup(sauce,'lxml')
    #soup = bs4.BeautifulSoup(r.text, 'lxml')
    #table1 =soup.find_all('table',{'class':'table table-striped scan_results_table dataTable.no-footer'})
    #table1 = soup.find_all('div',{'class': 'text-teal-700'})
    print(soup.contents)