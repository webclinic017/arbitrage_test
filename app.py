import streamlit as st
import datetime
from datetime import datetime as dt
import pandas as pd
import numpy as np
import ccxt
from backtesting import Backtest
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
df_btc = data_crawler.btc(startDate,end)


#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#BactTesting
#--------------------------------------------------
stats_df, result = simulation.bactest(Selectbox,df_btc)

if stats_df.empty :
    st.subheader(f'알고리즘 선택 필수!')
else :
    st.subheader(f'백테스팅 결과')
    st.bokeh_chart(result)      
    st.dataframe(stats_df.style.format({"E": "{:.2f}"}),width=1000,height=500)
    
# if Selectbox == 'SMA_CROSS' :
#     bt = Backtest(df_btc, SmaCross, cash=100_000, commission=.002)
#     stats = bt.run()
#     result = bt.plot(filename='./asset/backtesting_result',open_browser=False)
#     st.subheader(f'백테스팅 결과')
#     st.bokeh_chart(result)
    
#     stats_df = template.stats_df(stats)

#     st.dataframe(stats_df.style.format({"E": "{:.2f}"}),width=1000,height=500)

# else : st.subheader(f'알파값 입력 필수!')

