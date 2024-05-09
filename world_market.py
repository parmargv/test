import requests
import bs4
import urllib.parse
from urllib.request import Request, urlopen
import pandas as pd
from bs4 import BeautifulSoup as bs

def cash():
    url = "https://www.moneycontrol.com/stocks/marketstats/fii_dii_activity/index.php"
    headers = {}
    headers[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)

    soup = bs4.BeautifulSoup(resp, 'html.parser')
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
    def Bn_gainer(self):
        r = self.session.get(f"https://www.nseindia.com/api/live-analysis-variations?index=gainers",headers=self.headers).json()
        Bn_l = [data for data in r['BANKNIFTY']['data']]
        df = pd.DataFrame(Bn_l)
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
class money():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        self.session = requests.Session()
        self.session.get("https://www.moneycontrol.com/markets/global-indices/", headers=self.headers)

    def us_market(self):
        r = self.session.get(f"https://priceapi.moneycontrol.com/technicalCompanyData/globalMarket/getGlobalIndicesListingData?view=overview&deviceType=W",
                             headers=self.headers).json()
        us_market_data = next(item['data'] for item in r['dataList'] if item['heading'] == 'US_Market')
        columns = [item['name'] for item in r['header']]
        us_market_df = pd.DataFrame(us_market_data, columns=columns)
        selected_columns = ['name', 'price', 'net_change', 'percent_change']
        us_market_selected_df = us_market_df[selected_columns]
        return us_market_selected_df
    def euro_market(self):
        r = self.session.get(f"https://priceapi.moneycontrol.com/technicalCompanyData/globalMarket/getGlobalIndicesListingData?view=overview&deviceType=W",
                             headers=self.headers).json()
        euro_market_data = next(item['data'] for item in r['dataList'] if item['heading'] == 'European_Market')
        columns = [item['name'] for item in r['header']]
        us_market_df = pd.DataFrame(euro_market_data, columns=columns)
        selected_columns = ['name', 'price', 'net_change', 'percent_change']
        us_market_selected_df = us_market_df[selected_columns]
        return us_market_selected_df
    def asia_market(self):
        r = self.session.get(f"https://priceapi.moneycontrol.com/technicalCompanyData/globalMarket/getGlobalIndicesListingData?view=overview&deviceType=W",
                             headers=self.headers).json()
        asia_market_data = next(item['data'] for item in r['dataList'] if item['heading'] == 'Asian_Market')

        columns = [item['name'] for item in r['header']]
        us_market_df = pd.DataFrame(asia_market_data, columns=columns)
        selected_columns = ['name', 'price', 'net_change', 'percent_change']
        us_market_selected_df = us_market_df[selected_columns]
        return us_market_selected_df
class groww():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        self.session = requests.Session()
        self.session.get("https://groww.in/indices/global-indices", headers=self.headers)
    def Gobal_Indices(self):
        r = self.session.get(f"https://groww.in/v1/api/stocks_data/v1/global_instruments?instrumentType=GLOBAL_INSTRUMENTS",headers=self.headers).json()
        indices = [data for data in r['aggregatedGlobalInstrumentDto']]
        # nifty50_g = [data['PE'] for data in r['filtered']['data'] if "PE" in data]
        df = pd.DataFrame(indices)
        return df
def groww_data():
    d=groww()
    data=d.Gobal_Indices()
    giftnifty = data['livePriceDto']
    gnifty = (data['livePriceDto'][0])
    gift_ltp = int(gnifty['value'])
    gift_ch = int(gnifty['dayChange'])
    gift_per = (gnifty['dayChangePerc'])
    dow_f = (data['livePriceDto'][1])
    dowf_ltp = int(dow_f['value'])
    dowf_ch = int(dow_f['dayChange'])
    dowf_per = (dow_f['dayChangePerc'])
    dow = (data['livePriceDto'][3])
    dow_ltp = int(dow['value'])
    dow_ch = int(dow['dayChange'])
    dow_per = (dow['dayChangePerc'])
    nas = (data['livePriceDto'][2])
    nas_ltp = int(nas['value'])
    nas_ch = int(nas['dayChange'])
    nas_per = (nas['dayChangePerc'])
    sp=(data['livePriceDto'][4])
    sp_ltp = int(sp['value'])
    sp_ch = int(sp['dayChange'])
    sp_per = (sp['dayChangePerc'])
    nk=(data['livePriceDto'][5])
    nk_ltp = int(nk['value'])
    nk_ch = int(nk['dayChange'])
    nk_per = (nk['dayChangePerc'])
    hs=(data['livePriceDto'][6])
    hs_ltp = int(hs['value'])
    hs_ch = int(hs['dayChange'])
    hs_per = (hs['dayChangePerc'])
    dax=(data['livePriceDto'][7])
    dax_ltp = int(dax['value'])
    dax_ch = int(dax['dayChange'])
    dax_per = (dax['dayChangePerc'])
    ftse=(data['livePriceDto'][8])
    ftse_ltp = int(ftse['value'])
    ftse_ch = int(ftse['dayChange'])
    ftse_per = (ftse['dayChangePerc'])
    cac=(data['livePriceDto'][7])
    cac_ltp = int(cac['value'])
    cac_ch = int(cac['dayChange'])
    cac_per = (cac['dayChangePerc'])
    data = {
        "INDICES":['GIFT_NIFTY','DOW_FUT','DOW','NASDAQ','S&P','NIKKIE','HANG_SANG','DAX','FTSE','CAC'],
        "%":[gift_per,dowf_per,dow_per,nas_per,sp_per,nk_per,hs_per,dax_per,ftse_per,cac_per],
        "CHAGE":[gift_ch,dowf_ch,dow_ch,nas_ch,sp_ch,nk_ch,hs_ch,dax_ch,ftse_ch,cac_ch],
        "LTP":[gift_ltp,dowf_ltp,dow_ltp,nas_ltp,sp_ltp,nk_ltp,hs_ltp,dax_ltp,ftse_ltp,cac_ltp]
    }

    df = pd.DataFrame(data)
    return df


