import requests
import bs4
import pandas as pd
from pandas import ExcelWriter
from bs4 import BeautifulSoup
from openpyxl import load_workbook
import xlwings as xw
import time
import urllib3
import re
import urllib.parse
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from datetime import datetime

wb = xw.Book(r'C:\users\gvparmar\Desktop\a.xlsx')
sht = wb.sheets('NEWS')
sh2 = wb.sheets('LIVE')
sh3 = wb.sheets('chart')
str1 = 'yes'



url = 'https://chartink.com/screener/best-swing-trade-gvparmar'
headers = {
    'user-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"

}
r = requests.get(url, {'headers':headers})

soup = bs4.BeautifulSoup(r.text, 'html.parser')
table =soup.find_all('table')[1]
#h1 = soup.find_all('div',{'class':'col-xs-10'}).find_all('Table',{'class':'table table-striped scan_results_table DataTable no-footer'}).find_all('a').text



