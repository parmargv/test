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

    activity = ['Home','FII_data','Participant_Data']
    choice = st.sidebar.selectbox("Main Menu", activity)
    if choice=="Home":
        st_autorefresh(interval=60 * 1000, key="dataframerefresh")

        data = home.economics()
        n1 = data[0]
        n2 = data[1]
        n3 = data[2]
        n4 = data[3]
        data1 = home.cnbc()
        n5 = data1[0]
        n6 = data1[1]
        n7 = data1[2]
        n8 = data1[3]
        d11 = world_market.economics_data()
        data1 = d11.News()
        d22 = world_market.India_news()
        data2 = d22.News_india()

        d1 = data1['title'][0]
        d2 = data1['title'][1]
        d3 = data1['title'][2]
        d4 = data1['title'][3]
        d5 = data2['title'][0]
        d6 = data2['title'][1]
        d7 = data2['title'][2]
        d8 = data2['title'][3]
        gainer = world_market.fo()
        df11 = gainer.gainers()
        sk1_n = df11.iloc[0].iloc[0]
        st1_g = df11.iloc[0].iloc[2]
        sk2_n = df11.iloc[1].iloc[0]
        st2_g = df11.iloc[1].iloc[2]
        sk3_n = df11.iloc[2].iloc[0]
        st3_g = df11.iloc[2].iloc[2]
        sk4_n = df11.iloc[3].iloc[0]
        st4_g = df11.iloc[3].iloc[2]
        loosers = world_market.fo()
        df22 = loosers.loosers()
        sk1_na = df22.iloc[0].iloc[0]
        st1_l = df22.iloc[0].iloc[2]
        sk2_na = df22.iloc[1].iloc[0]
        st2_l = df22.iloc[1].iloc[2]
        sk3_na = df22.iloc[2].iloc[0]
        st3_l = df22.iloc[2].iloc[2]
        sk4_na = df22.iloc[3].iloc[0]
        st4_l = df22.iloc[3].iloc[2]
        nifty = world_market.OI_NIFTY()
        df1 = nifty.Nifty_gainer()
        nf1_n = (df1['symbol'][0])
        nf1_g = (df1['perChange'][0])
        nf2_n = (df1['symbol'][1])
        nf2_g = (df1['perChange'][1])
        nf3_n = (df1['symbol'][2])
        nf3_g = (df1['perChange'][2])
        nf4_n = (df1['symbol'][3])
        nf4_g = (df1['perChange'][3])

        df2 = nifty.Nifty_looser()
        nf1_na = (df2['symbol'][0])
        nf1_l = (df2['perChange'][0])
        nf2_na = (df2['symbol'][1])
        nf2_l = (df2['perChange'][1])
        nf3_na = (df2['symbol'][2])
        nf3_l = (df2['perChange'][2])
        nf4_na = (df2['symbol'][3])
        nf4_l = (df2['perChange'][3])
        df = home.bloomberg()
        bn1 = df[0][0]
        bn2 = df[0][1]
        bn3 = df[0][2]
        bn4 = df[0][3]
        bn5 = df[0][4]

        st.markdown(f'<marquee behavior="scroll" direction="left">Economics_times_news:-(1){n1}(2){n2}(3){n3}(4){n4}(5){n5}(6){n6}(7){n7}(8){n8}(9){bn1}(10){bn2}(11){bn3}(12){bn4}(13){bn5}(14){d1}(15){d2}(16){d3}(17){d4}</marquee>',unsafe_allow_html=True)
        st.markdown(
            f'<marquee behavior="scroll" direction="left">FO Gainers:(1){sk1_n}↑[{st1_g}](2){sk2_n}↑[{st2_g}](3){sk3_n}↑[{st3_g}](4){sk4_n}↑[{st4_g}]()'
            f'*******Nifty Gainers:(1){nf1_n}↑[{nf1_g}](2){nf2_n}↑[{nf2_g}](3){nf3_n}↑[{nf3_g}](4){nf4_n}↑[{nf4_g}]()FO Loosers:-(1){sk1_na}↓[{st1_l}](2){sk2_na}↓[{st2_l}](3){sk3_na}↓[{st3_l}](4){sk4_na}↓[{st4_l}]'
            f'()*******Nifty Loosers:-(1){nf1_na}↓[{nf1_l}](2){nf2_na}↓[{nf2_l}](3){nf3_na}↓[{nf3_l}](4){nf4_na}↓[{nf4_l}]()</marquee>',
            unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            gainer = world_market.fo()
            df11 = gainer.gainers()
            # sk1_n = df11.iloc[0].iloc[0]
            # st1_g = df11.iloc[0].iloc[2]
            # st1_oi = df11.iloc[0].iloc[3]
            # #print(df11.iloc[0][0],df11.iloc[0][1],df11.iloc[0][2])
            # st.markdown(f'<marquee behavior="scroll" direction="left" bgcolor="yellow">Top Gainers:-{sk1_n}({st1_g})({st1_oi})</marquee>',unsafe_allow_html=True)
            # st.markdown(f'<h1 style="color:#84CD0E;font-size:15px;">{"Top 10 F&O Gainers"}</h1>',
            #             unsafe_allow_html=True)

            st.markdown(f'<h1 style="color:#3f8c92;font-size:15px;">{"Top 10 F&O Gainers"}</h1>',
                        unsafe_allow_html=True)
            # st.markdown(f'<marquee behavior="scroll" direction="left">Here is some scrolling text... right to left!</marquee>', unsafe_allow_html=True)
            hide_table_row_index = """
                                                                                                                                                                                       <style>
                                                                                                                                                                                       tbody th {display:none}
                                                                                                                                                                                       .blank {display:none}
                                                                                                                                                                                       </style>
                                                                                                                                                                                       """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)

            st.table(df11.style.set_table_styles([{'selector': 'table', 'props': [('max-width', '100%')]}]))

        with col2:
            loosers = world_market.fo()
            df22 = loosers.loosers()

            # df22.set_index('OI(%)',inplace=False)
            st.markdown(f'<h1 style="color:#E11F2A;font-size:15px;">{"Top 10 F&O Losers"}</h1>', unsafe_allow_html=True)
            # st.markdown(f'<marquee behavior="scroll" direction="left">Here is some scrolling text... right to left!</marquee>', unsafe_allow_html=True)
            hide_table_row_index = """
                                                                                                                                                                           <style>
                                                                                                                                                                           tbody th {display:none}
                                                                                                                                                                           .blank {display:none}
                                                                                                                                                                           </style>
                                                                                                                                                                           """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)

            st.table(df22.style.set_table_styles([{'selector': 'table', 'props': [('max-width', '100%')]}]))
        col1, col2 = st.columns(2)
        with col1:
            nifty = world_market.OI_NIFTY()
            df1 = nifty.Nifty_gainer()
            df11 = df1.iloc[0:9, [0, 5, 6, 7]]
            # df11 = df1[['symblol', 'perChange']]
            # cols = ['symblol','perChange']
            # df11 = df1[df1.columns[cols]]
            # df_1=df_g['']
            df2 = nifty.Nifty_looser()
            df22 = df2.iloc[0:9, [0, 5, 6, 7]]
            # df22 = df2[df2.columns[cols]]
            st.markdown(f'<h1 style="color:#3f8c92;font-size:15px;">{"Nifty Gainers"}</h1>', unsafe_allow_html=True)
            # st.markdown(f'<marquee behavior="scroll" direction="left">Here is some scrolling text... right to left!</marquee>', unsafe_allow_html=True)
            hide_table_row_index = """
                                                                                                                                                                                       <style>
                                                                                                                                                                                       tbody th {display:none}
                                                                                                                                                                                       .blank {display:none}
                                                                                                                                                                                       </style>
                                                                                                                                                                                       """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            # df33 = df_g.iloc[0:1, 0:4]
            st.table(df11.style.set_table_styles([{'selector': 'table', 'props': [('max-width', '100%')]}]))
        with col2:
            st.markdown(f'<h1 style="color:#E11F2A;font-size:15px;">{"Nifty Loosers"}</h1>', unsafe_allow_html=True)
            # st.markdown(f'<marquee behavior="scroll" direction="left">Here is some scrolling text... right to left!</marquee>', unsafe_allow_html=True)
            hide_table_row_index = """
                                                                                                                                                                                                   <style>
                                                                                                                                                                                                   tbody th {display:none}
                                                                                                                                                                                                   .blank {display:none}
                                                                                                                                                                                                   </style>
                                                                                                                                                                                                   """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            # df44 = df_l.iloc[0:1, 0:4]
            st.table(df22.style.set_table_styles([{'selector': 'table', 'props': [('max-width', '100%')]}]))
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

    # if choice == "World_Market":
    #     st_autorefresh(interval=5 * 60 * 1000, key="dataframerefresh")
    #     df = world_market.Inveting()
    #     col1, col2 = st.columns(2)
    #     with col1:
    #         st.markdown(f'<h1 style="color:#D78A1B;font-size:25px;">{"Indices Future Asia"}</h1>',
    #                     unsafe_allow_html=True)
    #         hide_table_row_index = """
    #                                         <style>
    #                                         tbody th {display:none}
    #                                         .blank {display:none}
    #                                         </style>
    #                                         """
    #         st.markdown(hide_table_row_index, unsafe_allow_html=True)
    #         # ld =LiveData()
    #         df.drop(['checkbox', 'flag', 'Month', 'High', 'Low'], axis=1, inplace=True)
    #         df2 = df.iloc[20:26, 0:4]
    #         st.table(df2)
    #     with col2:
    #         st.markdown(f'<h1 style="color:#D78A1B;font-size:25px;">{"Indices Future US & Europe"}</h1>',
    #                     unsafe_allow_html=True)
    #
    #         df3 = df.iloc[2:10, 0:4]
    #         st.table(df3)

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


