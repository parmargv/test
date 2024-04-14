import base64
import urllib
from urllib.request import Request, urlopen
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import world_market
import home
import datetime
import pytz
from datetime import date

def main():
    st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
    india_timezone = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(india_timezone).time()
    today = date.today()
    today_name = today.strftime("%A")
    formatted_time = now.strftime("%H:%M:%S %Z")
    def news():
        st_autorefresh(interval=60 * 1000, key="dataframerefresh")
        data = home.economics()
        n1 = data[0]
        n2 = data[1]
        n3 = data[2]
        n4 = data[3]
        data1 = home.cnbc()
        n5 = data1[0][0]
        n6 = data1[0][1]
        n7 = data1[0][2]
        n8 = data1[0][3]
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

        df = home.bloomberg()
        bn1= df[0][0]
        bn2= df[0][1]
        bn3= df[0][2]
        bn4 = df[0][3]
        bn5 = df[0][4]

        st.markdown(f'<marquee behavior="scroll" direction="left">Economics_times_news:-(1){n1}(2){n2}(3){n3}(4){n4}()********CNBC_news(1){n5}(2){n6}(3){n7}(4){n8}....</marquee>',unsafe_allow_html=True)
        st.markdown(f'<marquee behavior="scroll" direction="left">Bloomberg_news:-(1){bn1}(2){bn2}(3){bn3}(4){bn4}(5){bn5}*******International_news(1){d1}(2){d2}(3){d3}(4){d4}******India_news(1){d5}(2){d6}(3){d7}(4){d8}()</marquee>',unsafe_allow_html=True)

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
    def market_movers():
        st_autorefresh(interval=60 * 1000, key="dataframerefresh")
        #st.markdown(f'<h1 style="color:#D78A1B;font-size:20px;">{"Nifty_Gainer_Looser"}</h1>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            gainer=world_market.fo()
            df11=gainer.gainers()

            st.markdown(f'<h1 style="color:#3f8c92;font-size:15px;">{"Top 10 F&O Gainers"}</h1>', unsafe_allow_html=True)
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
            loosers= world_market.fo()
            df22=loosers.loosers()

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
        col1, col2 = st.columns(2)
        with col1:
            nifty=world_market.OI_NIFTY()
            df1=nifty.Nifty_gainer()
            df11 =df1.iloc[0:9,[0,5,6,7]]
            df2=nifty.Nifty_looser()
            df22 =df2.iloc[0:9,[0,5,6,7]]
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
            #df33 = df_g.iloc[0:1, 0:4]
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
            #df44 = df_l.iloc[0:1, 0:4]
            st.table(df22.style.set_table_styles([{'selector': 'table', 'props': [('max-width', '100%')]}]))

    def world_m():
        st_autorefresh(interval=1 * 60 * 1000, key="dataframerefresh")
        wm = world_market.money()
        df_us = wm.us_market()
        df_eu =wm.euro_market()
        df_asia=wm.asia_market()

        col1, col2,col3= st.columns(3)
        with col1:
            st.markdown(f'<h1 style="color:#D78A1B;font-size:25px;">{"Indices us market"}</h1>',unsafe_allow_html=True)
            st.table(df_us)
        with col2:
            st.markdown(f'<h1 style="color:#D78A1B;font-size:25px;">{"Indices Europe"}</h1>',unsafe_allow_html=True)
            st.table(df_eu)
        with col3:
            st.markdown(f'<h1 style="color:#D78A1B;font-size:25px;">{"Indices asian market"}</h1>',unsafe_allow_html=True)
            st.table(df_asia)
    def FII_data():
        df = world_market.cash()
        hide_table_row_index = """
                                                                                <style>
                                                                                tbody th {display:none}
                                                                                .blank {display:none}
                                                                                </style>
                                                                                """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)

    def participant_data():
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
            df2.loc['Net Option position']=df2.loc['Index call']-df2.loc['Index put']
            first_7_rows = df2.head(1)
            last_7_rows = df2.tail(7)
            df = pd.concat([first_7_rows, last_7_rows])
            df = df.drop(df.columns[-1], axis=1)
            st.table(df)

    #st.markdown(f'<marquee behavior="scroll" direction="left">Current_Time:{formatted_time},Today:-{today_name},Login_state:-{login_state},User_Name:{user_name}</marquee>', unsafe_allow_html=True)
    col1, col2, col3 ,col4 = st.columns(4)
    with col1:
        st.write(f"Last updated time: {formatted_time}")
    with col2:
        st.write(f"Today is: {today_name}")

    activity = ['Home', 'Market_data']

    # Define submenu options for each main menu option
    submenus = {
        'Home': None,
        'Market_data': ['News','Market_movers','World_Market','FII_data','Participant_Data'],
    }

    # Get the selected main menu option
    selected_main_menu = st.sidebar.selectbox("Main Menu", activity)
    selected_submenu = None

    if selected_main_menu in submenus:
        # Check if submenus[selected_main_menu] is not None
        if submenus[selected_main_menu] is not None:
            selected_submenu = st.sidebar.selectbox("Submenu", submenus[selected_main_menu])
            st.write(f"You selected: {selected_main_menu} -> {selected_submenu}")
        else:
            st.write(f"No submenu options available for {selected_main_menu}")
    else:
        st.write(f"You selected: {selected_main_menu}")
    # Initialize selected_submenu to None
    # If the selected main menu option has submenus, display them


    if selected_main_menu=="Home":
        st_autorefresh(interval=30 * 1000, key="dataframerefresh")
        background_color = """
        <style>
        body {
            background-color: #008080; /* Replace with your desired color code */
        }
        </style>
        """

        st.markdown(background_color, unsafe_allow_html=True)
        st.markdown(f'<h1 style="color:#228b22;font-size:20px;">{"Welcome to Market News!!"}</h1>', unsafe_allow_html=True)

        st.image('stock1.jpg', caption='Market at Home',use_column_width="wide")
    if selected_submenu == "News":
        news()
    elif selected_submenu == "Market_movers":
        market_movers()
    elif selected_submenu == "World_Market":
        world_m()
    elif selected_submenu == "FII_data":
        FII_data()
    elif selected_submenu == "Participant_Data":
        participant_data()
    else:
        st.write(f"You selected: {selected_main_menu}")

if __name__ == "__main__":
    india_timezone = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(india_timezone).time()
    current_day = datetime.datetime.today().weekday()
    main()
