import pandas as pd
import numpy as np
from selenium import webdriver
from pandas import ExcelWriter
import xlwings as xw
import time
from datetime import datetime
import os

wb = xw.Book(r'C:\users\gvparmar\Desktop\a.xlsx')
sht = wb.sheets('NEWS')
sh2 = wb.sheets('LIVE')
sh3 = wb.sheets('chart')


#url ='https://chartink.com/screener/best-swing-trade-gvparmar'
url ='https://chartink.com/screener/bestswing-trade-cash-gvparmar'

driver = webdriver.Chrome(executable_path=r'C:\Users\gvparmar\Desktop\chromedriver.exe')
driver.get(url)
table1 = pd.read_html(driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]').get_attribute('outerHTML'))

#table.drop(['Sr.', 'Stock Name', 'Link'], axis=1, inplace=True)
tb1 =table1[0]


driver.close()
os.system("taskkill /im Chrome.exe /f")
sh3.range('A1:H20').value =0
sh3.range('A1').value = table1




