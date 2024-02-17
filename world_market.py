import requests

import urllib.parse
from urllib.request import Request, urlopen
import pandas as pd
from bs4 import BeautifulSoup as bs

# def Inveting():
#     # ----------------------INVESTING STOCK LIVE----------------------------------
#     url = "https://in.investing.com/indices/indices-futures"
#     headers = {}
#     headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
#
#     req = urllib.request.Request(url, headers=headers)
#     resp = urllib.request.urlopen(req)
#     print(resp)  # This will print infor
    # content = resp.read()  # Read the response content
    # soup = bs4.BeautifulSoup(content, 'html.parser')


    # soup = bs4.BeautifulSoup(resp, 'html.parser')
    # table = soup.find('div', {'class': 'common-table-scroller js-table-scroller'})
    # trs = table.find_all('tr')
    # rows = []
    # columns = ['checkbox', 'flag', 'Name', 'Month', 'Last', 'High', 'Low', 'Chg', 'Chg(%)', 'Time']
    # for tr in trs[1:]:
    #     tds = tr.find_all('td')
    #     row = [td.text.replace('\n', '').strip() for td in tds]
    #     rows.append(row)
    # df = pd.DataFrame(rows, columns=columns)
    # return df


def cash():
    url = "https://www.moneycontrol.com/stocks/marketstats/fii_dii_activity/index.php"
    headers = {}
    headers[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)

    soup = bs(resp, 'html.parser')
    table3 = soup.find('div', {'class': 'fidi_tbescrol table-responsive'})
    trs = table3.find_all('tr')
    rows = []
    columns = ['DATE', 'FII_BUY', 'FII_SELL', 'FII_NET', 'DII_BUY', 'DII_SELL', 'DII_NET']
    for tr in trs[1:]:
        tds = tr.find_all('td')
        row = [td.text.replace('\n', '').strip() for td in tds]
        rows.append(row)
    df3 = pd.DataFrame(rows, columns=columns)
    df3['DATE'] = df3['DATE'].astype(str)
    df3['DATE'] = df3['DATE'].str[0:11]
    # df3['FII_SELL'] = df3['FII_SELL'].astype('int64')
    # df3 = df3.astype({"FII_SELL": 'str'})
    # df3['FII_SELL']=pd.to_numeric(df3['FII_SELL'],downcast='signed')
    df = df3[2:]
    # df = df.reset_index()
    # df.sort_index(axis=0,ascending=False)
    return (df)


class OI_NIFTY:

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        self.session = requests.Session()
        self.session.get("http://nseindia.com", headers=self.headers)

    def Nifty_gainer(self):
        r = self.session.get(f"https://www.nseindia.com/api/live-analysis-variations?index=gainers",headers=self.headers).json()
        niftyg = [data for data in r['NIFTY']['data']]
        # nifty50_g = [data['PE'] for data in r['filtered']['data'] if "PE" in data]
        df = pd.DataFrame(niftyg)
        return df

    def Nifty_looser(self):
        r = self.session.get(f"https://www.nseindia.com/api/live-analysis-variations?index=loosers",headers=self.headers).json()
        niftyl = [data for data in r['NIFTY']['data']]
        # nifty50_g = [data['PE'] for data in r['filtered']['data'] if "PE" in data]
        df = pd.DataFrame(niftyl)
        return df

    def Bn_looser(self):
        r = self.session.get(f"https://www.nseindia.com/api/live-analysis-variations?index=loosers",headers=self.headers).json()
        Bn_l = [data for data in r['BANKNIFTY']['data']]
        df = pd.DataFrame(Bn_l)
        return df

class economics_data():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        self.session = requests.Session()
        self.session.get("https://tradingeconomics.com/stream", headers=self.headers)

    def News(self):
        r = self.session.get(f"https://tradingeconomics.com/ws/stream.ashx?start=0&size=20",headers=self.headers).json()
        news = [title for title in r]
        df = pd.DataFrame(news)
        return df
class India_news():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        self.session = requests.Session()
        self.session.get("https://tradingeconomics.com/india/news", headers=self.headers)
    def News_india(self):
        r = self.session.get(f"https://tradingeconomics.com/ws/stream.ashx?start=0&size=20&c=india",headers=self.headers).json()
        news = [title for title in r]
        df = pd.DataFrame(news)
        return df
class fo():
    def gainers(self):
        url = "https://www.moneycontrol.com/stocks/fno/marketstats/futures/gainers/homebody.php?opttopic=gainers&optinst=stkfut&sel_mth=1&sort_order=0"
        headers = {}
        headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)

        soup = bs(resp, 'html.parser')
        table1 = soup.find('div', {'class': 'MT15'})
        trs = table1.find_all('tr')
        rows = []
        columns = ['SYMB', 'EXP', 'LTP', 'CH', 'CH(%)', 'H-L', 'AVG', 'VOL', 'VALUE', 'OI', 'OI-CH']
        for tr in trs[1:]:
            tds = tr.find_all('td')
            row = [td.text.replace('\n', '').strip() for td in tds]
            rows.append(row)
        df1 = pd.DataFrame(rows, columns=columns)
        df1.drop(['VALUE'], axis=1, inplace=True)
        df1.reset_index(drop=True, inplace=False)

        oi = df1['OI-CH'].str.split("\r", expand=True)

        vol = df1['VOL'].str.split("\r\t\t\t\t\t\t\t\t", expand=True)
        df1.drop(['EXP', 'CH', 'H-L', 'AVG', 'OI-CH', 'VOL'], axis=1, inplace=True)
        df1["OI"] = oi[0]
        df1["OI(%)"] = oi[1]
        df1.drop(['OI'], axis=1, inplace=True)
        df1["VOL"] = vol[0]
        df11 = df1.iloc[0:10, 0:4]
        return df11
    def loosers(self):
        url = "https://www.moneycontrol.com/stocks/fno/marketstats/futures/losers/homebody.php?opttopic=losers&optinst=stkfut&sel_mth=1&sort_order=0"
        headers = {}
        headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)

        soup = bs(resp, 'html.parser')
        table2 = soup.find('div', {'class': 'MT15'})
        trs = table2.find_all('tr')
        rows = []
        columns = ['SYMB', 'EXP', 'LTP', 'CH', 'CH(%)', 'H-L', 'AVG', 'VOL', 'VALUE', 'OI', 'OI-CH']
        for tr in trs[1:]:
            tds = tr.find_all('td')
            row = [td.text.replace('\n', '').strip() for td in tds]
            rows.append(row)
        df2 = pd.DataFrame(rows, columns=columns)

        df2.drop(['VALUE'], axis=1, inplace=True)
        df2.reset_index(drop=True, inplace=False)
        oi = df2['OI-CH'].str.split("\r", expand=True)
        vol = df2['VOL'].str.split("\r\t\t\t\t\t\t\t\t", expand=True)
        df2.drop(['EXP', 'CH', 'H-L', 'AVG', 'OI-CH', 'VOL'], axis=1, inplace=True)
        df2["OI"] = oi[0]
        df2["OI(%)"] = oi[1]
        df2.drop(['OI'], axis=1, inplace=True)
        # df2["VOL"] = vol[0]
        df22 = df2.iloc[0:10, 0:4]
        return df22



# d=economics_data()
# data=d.News()
# print(data['title'][1])
