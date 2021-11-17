import streamlit as st
import datetime
from datetime import datetime as dt
import pandas as pd
import ccxt
from backtesting import Backtest
from utils.SMA import SmaCross

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


startDate = dt.strptime(str(start_date), "%Y-%m-%d")
startDate = int(dt.timestamp(startDate)) * 1000
end = start_date - end_date

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#BTC 가격
#--------------------------------------------------
binance = ccxt.binance()
ohlcvs = binance.fetch_ohlcv('BTC/USDT', timeframe='1d', since=startDate, limit=100)

for idx, ohlcv in enumerate(ohlcvs):
    ohlcvs[idx] = [dt.fromtimestamp(ohlcv[0]/1000).strftime('%Y-%m-%d %H:%M:%S'), ohlcv[1], ohlcv[2], ohlcv[3], ohlcv[4],ohlcv[5]]

df_btc = pd.DataFrame(ohlcvs)
df_btc.columns = ['Time', 'Open','High','Low','Close','Volume']
df_btc['Time'] = pd.to_datetime(df_btc['Time'], format='%Y-%m-%d %H:%M:%S', errors='raise')
df_btc = df_btc[df_btc['Time'] >= '2021-06-24'].reset_index(drop = True)
df_btc.set_index('Time',inplace=True)


#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#BactTesting
#--------------------------------------------------
bt = Backtest(df_btc, SmaCross, cash=100_000, commission=.002)
stats = bt.run()

result = bt.plot(filename='./asset/backtesting_result',open_browser=False)

st.subheader(f'백테스팅 결과')
st.bokeh_chart(result)


