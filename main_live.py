import os
import urllib
import bs4
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import requests
import streamlit as st
from streamlit_autorefresh import st_autorefresh
#import chartink
import pandas as pd
import sqlite3
import world_market
import home
import datetime
from datetime import date
import pytz

def main():
    st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
    india_timezone = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(india_timezone).time()
    today = date.today()
    today_name = today.strftime("%A")
    formatted_time = now.strftime("%H:%M:%S %Z")

    #st.markdown(f'<marquee behavior="scroll" direction="left">Current_Time:{formatted_time},Today:-{today_name},Login_state:-{login_state},User_Name:{user_name}</marquee>', unsafe_allow_html=True)

    activity = ['Home','News','Future_stocks','World_Market','FII_data','Participant_Data']
    choice = st.sidebar.selectbox("Main Menu", activity)
    if choice=="Home":
        st_autorefresh(interval=10 * 1000, key="dataframerefresh")
        background_color = """
        <style>
        body {
            background-color: #008080; /* Replace with your desired color code */
        }
        </style>
        """

        st.markdown(background_color, unsafe_allow_html=True)
        st.title("My Algo Trading App")
        st.markdown(f'<h1 style="color:#228b22;font-size:20px;">{"Welcome to Algo trading!"}</h1>', unsafe_allow_html=True)

        # st.image('stock.jpg', caption='Market at Home',use_column_width="wide")

    if choice == "News":
        st_autorefresh(interval=60 * 1000, key="dataframerefresh")
        data = home.economics()
        n1 = data[0]
        n2 = data[1]
        n3 = data[2]
        n4 = data[3]
        data = home.economics()
        n1=data[0]
        n2=data[1]
        n3=data[2]
        n4=data[3]
        data1 = home.cnbc()
        n5 = data1[0]
        n6 = data1[1]
        n7 = data1[2]
        n8 = data1[3]
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

        d = economics_data()
        data=d.News()
        d1=(data['title'][0])
        d2 = (data['title'][1])
        d3 = (data['title'][2])
        d4 = (data['title'][3])
        d5 = (data['title'][4])
        class India_news():
            def __init__(self):
                self.headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
                self.session = requests.Session()
                self.session.get("https://tradingeconomics.com/india/news", headers=self.headers)

            def News_india(self):
                r = self.session.get(f"https://tradingeconomics.com/ws/stream.ashx?start=0&size=20&c=india",
                                     headers=self.headers).json()
                news = [title for title in r]
                df = pd.DataFrame(news)
                return df

        d = India_news()
        data = d.News_india()
        d6 = (data['title'][0])
        d7 = (data['title'][1])
        d8 = (data['title'][2])
        d9 = (data['title'][3])
        d10 = (data['title'][4])
        st.markdown(f'<marquee behavior="scroll" direction="left">Market news:-(1){n1}(2){n2}(3){n3}(4){n4}(5){n5}(6){n6}(7){n7}(8){n8}______International news(1){d1}(2){d2}(3){d3}(4){d4}(5){d5}______________India_Live_news(1){d6}(2){d7}(3){d8}(4){d9}(5){d10}</marquee>',unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            df = home.bloomberg()
            hide_table_row_index = """
                                                                                                                                                                          <style>
                                                                                                                                                                          tbody th {display:none}
                                                                                                                                                                          .blank {display:none}
                                                                                                                                                                          </style>
                                                                                                                                                                          """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)

            th_props = [
                ('font-size', '17px'),
                ('text-align', 'center'),
                # ('font-weight', 'bold'),
                ('color', '#FF7F50'),

            ]

            td_props = [
                ('font-size', '17px'),
                ('color', '#2E8B57'),
            ]

            styles = [
                dict(selector="th", props=th_props),
                dict(selector="td", props=td_props)
            ]

            df2 = df.style.set_properties(**{'text-align': 'left'}).set_table_styles(styles)
            st.table(df2)
        with col2:
            df = home.investing()
            hide_table_row_index = """
                                                                                                                                                                          <style>
                                                                                                                                                                          tbody th {display:none}
                                                                                                                                                                          .blank {display:none}
                                                                                                                                                                          </style>
                                                                                                                                                                          """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)

            th_props = [
                ('font-size', '17px'),
                ('text-align', 'center'),
                # ('font-weight', 'bold'),
                ('color', '#FF7F50'),

            ]

            td_props = [
                ('font-size', '17px'),
                ('color', '#2E8B57'),
            ]

            styles = [
                dict(selector="th", props=th_props),
                dict(selector="td", props=td_props)
            ]

            df2 = df.style.set_properties(**{'text-align': 'left'}).set_table_styles(styles)
            st.table(df2)

        col1, col2 = st.columns(2)
        with col1:
            df = home.bt()
            hide_table_row_index = """
                                                                                                                                                                          <style>
                                                                                                                                                                          tbody th {display:none}
                                                                                                                                                                          .blank {display:none}
                                                                                                                                                                          </style>
                                                                                                                                                                          """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)

            th_props = [
                ('font-size', '17px'),
                ('text-align', 'center'),
                # ('font-weight', 'bold'),
                ('color', '#FF7F50'),

            ]

            td_props = [
                ('font-size', '17px'),
                ('color', '#2E8B57'),
            ]

            styles = [
                dict(selector="th", props=th_props),
                dict(selector="td", props=td_props)
            ]

            df2 = df.style.set_properties(**{'text-align': 'left'}).set_table_styles(styles)
            st.table(df2)
        with col2:
            df = home.earning()
            hide_table_row_index = """
                                                                                                                                                                                      <style>
                                                                                                                                                                                      tbody th {display:none}
                                                                                                                                                                                      .blank {display:none}
                                                                                                                                                                                      </style>
                                                                                                                                                                                      """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)

            th_props = [
                ('font-size', '17px'),
                ('text-align', 'center'),
                # ('font-weight', 'bold'),
                ('color', '#FF7F50'),

            ]

            td_props = [
                ('font-size', '17px'),
                ('color', '#2E8B57'),
            ]

            styles = [
                dict(selector="th", props=th_props),
                dict(selector="td", props=td_props)
            ]

            df2 = df.style.set_properties(**{'text-align': 'left'}).set_table_styles(styles)
            st.table(df2)

    if choice == 'FO_data':
        st_autorefresh(interval=60 * 1000, key="dataframerefresh")
        #st.markdown(f'<h1 style="color:#D78A1B;font-size:20px;">{"Nifty_Gainer_Looser"}</h1>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            url = "https://www.moneycontrol.com/stocks/fno/marketstats/futures/gainers/homebody.php?opttopic=gainers&optinst=stkfut&sel_mth=1&sort_order=0"
            headers = {}
            headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
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
            # sk1_n = df11.iloc[0].iloc[0]
            # st1_g = df11.iloc[0].iloc[2]
            # st1_oi = df11.iloc[0].iloc[3]
            # #print(df11.iloc[0][0],df11.iloc[0][1],df11.iloc[0][2])
            # st.markdown(f'<marquee behavior="scroll" direction="left" bgcolor="yellow">Top Gainers:-{sk1_n}({st1_g})({st1_oi})</marquee>',unsafe_allow_html=True)
            # st.markdown(f'<h1 style="color:#84CD0E;font-size:15px;">{"Top 10 F&O Gainers"}</h1>',
            #             unsafe_allow_html=True)
            hide_table_row_index = """
                                                                                                                                                                   <style>
                                                                                                                                                                   tbody th {display:none}
                                                                                                                                                                   .blank {display:none}
                                                                                                                                                                   </style>
                                                                                                                                                                   """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)

            st.table(df11.style.set_table_styles([{'selector': 'table', 'props': [('max-width', '100%')]}]))
        with col2:
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

            #df22.set_index('OI(%)',inplace=False)
            st.markdown(f'<h1 style="color:#E11F2A;font-size:15px;">{"Top 10 F&O Losers"}</h1>', unsafe_allow_html=True)
            #st.markdown(f'<marquee behavior="scroll" direction="left">Here is some scrolling text... right to left!</marquee>', unsafe_allow_html=True)
            hide_table_row_index = """
                                                                                                                                                                   <style>
                                                                                                                                                                   tbody th {display:none}
                                                                                                                                                                   .blank {display:none}
                                                                                                                                                                   </style>
                                                                                                                                                                   """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)

            st.table(df22.style.set_table_styles([{'selector': 'table', 'props': [('max-width', '100%')]}]))


    if choice == "World_Market":
        st_autorefresh(interval=5 * 60 * 1000, key="dataframerefresh")
        df = world_market.Inveting()
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f'<h1 style="color:#D78A1B;font-size:25px;">{"Indices Future Asia"}</h1>',
                        unsafe_allow_html=True)
            hide_table_row_index = """
                                            <style>
                                            tbody th {display:none}
                                            .blank {display:none}
                                            </style>
                                            """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            # ld =LiveData()
            df.drop(['checkbox', 'flag', 'Month', 'High', 'Low'], axis=1, inplace=True)
            df2 = df.iloc[20:26, 0:4]
            st.table(df2)
        with col2:
            st.markdown(f'<h1 style="color:#D78A1B;font-size:25px;">{"Indices Future US & Europe"}</h1>',
                        unsafe_allow_html=True)

            df3 = df.iloc[2:10, 0:4]
            st.table(df3)

    if choice == 'FII_data':
        df = world_market.cash()
        hide_table_row_index = """
                                                                                <style>
                                                                                tbody th {display:none}
                                                                                .blank {display:none}
                                                                                </style>
                                                                                """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    if choice=="Participant_Data":
        d = st.date_input("Enter Date", datetime.date(2023, 12, 22))
        st.write('Selected Date is:', d)
        option = st.selectbox(
            'Date is ok?',('NO', 'YES'))
        if option=="YES":
            t = d.strftime("%d%m%Y")
            url = f"https://archives.nseindia.com/content/nsccl/fao_participant_oi_" + str(t) + ".csv"

            headers = {}
            headers[
                'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            df = pd.read_csv(f"https://archives.nseindia.com/content/nsccl/fao_participant_oi_" + str(t) + ".csv",skiprows=1)
            df2 = df.T
            df2.loc['Future index'] = df2.loc['Future Index Long'] - df2.loc['Future Index Short']
            df2.loc['Future stock'] = df2.loc['Future Stock Long'] - df2.loc['Future Stock Short\t']
            df2.loc['Index call'] = df2.loc['Option Index Call Long'] - df2.loc['Option Index Call Short']
            df2.loc['Index put'] = df2.loc['Option Index Put Long'] - df2.loc['Option Index Put Short']
            df2.loc['Stock call'] = df2.loc['Option Stock Call Long'] - df2.loc['Option Stock Call Short']
            df2.loc['Stock put'] = df2.loc['Option Stock Put Long'] - df2.loc['Option Stock Put Short']
            first_6_rows = df2.head(1)
            last_6_rows = df2.tail(6)
            df = pd.concat([first_6_rows, last_6_rows])
            df = df.drop(df.columns[-1], axis=1)
            st.table(df)

if __name__ == "__main__":
    india_timezone = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(india_timezone).time()
    current_day = datetime.datetime.today().weekday()
    main()


