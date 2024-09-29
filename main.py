import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import world_market
import home
import datetime
import os
import pytz
from datetime import date

def main():
    st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
    activity = ['Home','News','Market_movers','view_morning_stocks','World_Market','FII_data']
    choice = st.sidebar.selectbox("Main Menu", activity)

    if choice =='Home':
        st.write("# Welcome to Streamlit! 👋")
        st.markdown(f'<h1 style="color:#228b22;font-size:20px;">{"Welcome to Market News!!"}</h1>',unsafe_allow_html=True)
        # st.image('stock1.jpg', caption='Market at Home', use_column_width="wide")
        india_timezone = pytz.timezone('Asia/Kolkata')
        now = datetime.datetime.now(india_timezone).time()
        today = date.today()
        today_name = today.strftime("%A")
        formatted_time = now.strftime("%H:%M:%S %Z")

        def save_stock_at_morning():
            absolute_path = os.path.dirname(__file__)

            df_data = world_market.run_at_morning()
            df_1 = df_data[2]
            df_2 = df_data[3]

            file_path = os.path.join(absolute_path, 'gainer.csv')
            with open(file_path, 'w') as file:
                file.write("")
                df_1.to_csv(file_path, index=False)

            file_path = os.path.join(absolute_path, 'looser.csv')
            with open(file_path, 'w') as file:
                file.write("")
                df_2.to_csv(file_path, index=False)
            st.text("Stocks data saved")

        st_autorefresh(interval=60 * 1000, key="dataframerefresh")
        current_time = datetime.datetime.now(india_timezone).time()
        st.text(current_time)
        morning_time1 = datetime.time(9, 30)
        morning_time2 = datetime.time(9, 32)

        if (morning_time1 <= current_time <= morning_time2):
            save_stock_at_morning()

    if choice == 'News':
        st_autorefresh(interval=60 * 1000, key="dataframerefresh")
        col1, col2, col3 = st.columns(3)
        with col1:
            df1 = home.economics()
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

            df2 = df1.style.set_properties(**{'text-align': 'left'}).set_table_styles(styles)
            st.table(df2)
        with col2:
            df2 = home.cnbc()
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

            df2 = df2.style.set_properties(**{'text-align': 'left'}).set_table_styles(styles)
            st.table(df2)
        with col3:
            df5 = home.bloomberg()
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

            df3 = df5.style.set_properties(**{'text-align': 'left'}).set_table_styles(styles)
            st.table(df3)

    if choice == 'Market_movers':
        st_autorefresh(interval=30 * 1000, key="dataframerefresh")
        #st.markdown(f'<h1 style="color:#D78A1B;font-size:20px;">{"Nifty_Gainer_Looser"}</h1>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            nse_data = world_market.run_at_morning()
            df11=nse_data[0]

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
            nse_data = world_market.run_at_morning()
            df22 = nse_data[1]

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

    if choice == 'World_Market':
        st_autorefresh(interval=1 * 30 * 1000, key="dataframerefresh")
        wm = world_market.money()
        df_us = wm.us_market()
        df_eu =wm.euro_market()
        df_asia=wm.asia_market()
        df1 = world_market.groww_data()
        st.table(df1)

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


    if choice == 'view_morning_stocks':
        absolute_path = os.path.dirname(__file__)
        file_path = 'gainer.csv'
        gainer_df = pd.read_csv(file_path)
        st.text("Gainers.............at..........9.30....")
        st.table(gainer_df)
        file_path = 'looser.csv'
        looser_df = pd.read_csv(file_path)
        st.text("Looser..............at..........9.30....")
        st.table(looser_df)



    # # Get the selected main menu option
    # selected_main_menu = st.sidebar.selectbox("Main Menu", activity)
    # selected_submenu = None
    #
    # if selected_main_menu in submenus:
    #     # Check if submenus[selected_main_menu] is not None
    #     if submenus[selected_main_menu] is not None:
    #         selected_submenu = st.sidebar.selectbox("Submenu", submenus[selected_main_menu])
    #         st.write(f"You selected: {selected_main_menu} -> {selected_submenu}")
    #     else:
    #         st.write(f"No submenu options available for {selected_main_menu}")
    # else:
    #     st.write(f"You selected: {selected_main_menu}")
    # # Initialize selected_submenu to None
    # # If the selected main menu option has submenus, display them
    #
    #
    # if selected_main_menu=="Home":
    #     st.write("# Welcome to Streamlit! 👋")
    #     st_autorefresh(interval=30 * 1000, key="dataframerefresh")
    #     st.markdown(f'<h1 style="color:#228b22;font-size:20px;">{"Welcome to Market News!!"}</h1>', unsafe_allow_html=True)
    #     st.image('stock1.jpg', caption='Market at Home',use_column_width="wide")
    #     india_timezone = pytz.timezone('Asia/Kolkata')
    #     now = datetime.datetime.now(india_timezone).time()
    #     today = date.today()
    #     today_name = today.strftime("%A")
    #     formatted_time = now.strftime("%H:%M:%S %Z")
    #     current_time = datetime.datetime.now(india_timezone).time()
    #     morning_time1 = datetime.time(9, 30)
    #     morning_time2 = datetime.time(9, 35)
    #
    #     if (morning_time1 <= current_time <= morning_time2):
    #         save_stock_at_morning()
    #
    # if selected_submenu == "News":
    #     news()
    # elif selected_submenu == "Market_movers":
    #     market_movers()
    # elif selected_submenu == "World_Market":
    #     world_m()
    #     save_stock_at_morning()
    # elif selected_submenu == "FII_data":
    #     FII_data()
    #     save_stock_at_morning()
    # elif selected_submenu == "view_morning_stocks":
    #     view_morning_stocks()
    # else:
    #     st.write(f"You selected: {selected_main_menu}")

if __name__ == "__main__":
    # india_timezone = pytz.timezone('Asia/Kolkata')
    # current_time = datetime.datetime.now(india_timezone).time()
    # current_day = datetime.datetime.today().weekday()
    main()
