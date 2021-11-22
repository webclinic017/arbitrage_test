import streamlit as st
import datetime
# from datetime import datetime as dt
# import pandas as pd
# import numpy as np
# import ccxt
# from backtesting import Backtest
from utils.Alpha_Function import SmaCross
from utils import data_crawler
from utils import template
from utils import simulation

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Set Template
#--------------------------------------------------
startDate, end, money,Selectbox = template.Template()
    
#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Data input
#--------------------------------------------------
df_klay = data_crawler.klay(startDate,end)
df_btc = data_crawler.btc(startDate,end)

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#BactTesting
#--------------------------------------------------

stats_klay, result_klay = simulation.bactest(Selectbox,df_klay)
stats_btc, result_btc = simulation.bactest(Selectbox,df_btc)

if stats_btc.empty :
    st.subheader(f'알고리즘 선택 필수!')
else :
    st.subheader(f'백테스팅 결과(Klay 매도)')
    st.bokeh_chart(result_klay)       
    st.subheader(f'백테스팅 결과(bitcoin 매수)')
    st.bokeh_chart(result_btc)      
    st.dataframe(stats_btc.style.format({"E": "{:.2f}"}),width=1000,height=500)

