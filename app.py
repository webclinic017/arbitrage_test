import streamlit as st
import datetime
from datetime import datetime as dt
import pandas as pd
import numpy as np
import ccxt
from backtesting import Backtest
from utils.Alpha_Function import SmaCross
from utils import data_crawler
#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
# Set page-config
#--------------------------------------------------
st.set_page_config(page_title="AI_LAB",page_icon="📍", layout="centered", initial_sidebar_state='expanded')

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
# Set style
#--------------------------------------------------
st.markdown(
    """
    <style>
    .reportview-container {
        background: #EBECE5
    }
    a:link{ color:#325FE5; } 
    a:visited{ color:#325FE5; } 
    a:hover{ color:#325FE5; } 
    a:active{ color:#325FE5}
    </style>
    """,
    unsafe_allow_html=True
)

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
# Title and Sub-title
#--------------------------------------------------
st.markdown(
    """
    <center>
        <h1>백테스팅 테스트</h1>
    </center>
    """,
    unsafe_allow_html=True
)

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
# Sidebar Setup
#--------------------------------------------------

with st.sidebar.form(key="my_form"):
    st.markdown("**운용기간**")
    start_date = st.date_input("시작일", datetime.date(2021, 7, 1),help = '`Select` start_date to get started 😏')
    end_date = st.date_input("종료일", datetime.date.today(),help = '`Select` end_date to get started 😏')

    st.markdown("**운용자금**")
    money = st.number_input("운용자금",
            value=100_000,
            min_value=100_000,
            help = '`Select` money to get started 😏')
    pressed = st.form_submit_button("Run")

with st.sidebar.form(key="my_form1"):
    st.subheader('**알파알고리즘**')
    SMA_alpha = st.checkbox('이동평균선_Test', value=True)
    en_beta = st.checkbox('인핸스드 베타', value=True)
    al_beta = st.checkbox('대체 베타', value=False)
    pu_alpa = st.checkbox('퓨어 알파', value=False)
    
    st.subheader('**리스크알고리즘**')
    beta = st.checkbox('기대수익률', value=True)
    en_beta = st.checkbox('상관관계', value=True)
    al_beta = st.checkbox('캐리', value=False)
    pu_alpa = st.checkbox('손절매', value=False)
    pressed2 = st.form_submit_button("Run")


startDate = dt.strptime(str(start_date), "%Y-%m-%d")
startDate = int(dt.timestamp(startDate)) * 1000
end = (end_date - start_date).days
if end > 1000 :
    end = 1000

#Data input
df_btc = data_crawler.btc(startDate,end)


#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#BactTesting
#--------------------------------------------------

if SMA_alpha :
    bt = Backtest(df_btc, SmaCross, cash=100_000, commission=.002)
    stats = bt.run()
    result = bt.plot(filename='./asset/backtesting_result',open_browser=False)
    st.subheader(f'백테스팅 결과')
    st.bokeh_chart(result)

else : st.subheader(f'알파값 입력 필수!')
