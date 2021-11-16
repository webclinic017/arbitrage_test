import streamlit as st
import datetime
from datetime import datetime as dt
import pandas as pd
import ccxt
from backtesting import Backtest
from SMA import SmaCross
# App title
st.markdown('''
# 백테스팅 테스트
''')


# Sidebar
start_date = st.sidebar.date_input("Start date", datetime.date(2021, 7, 1))
end_date = st.sidebar.date_input("End date", datetime.date.today())

startDate = dt.strptime(str(start_date), "%Y-%m-%d")
startDate = int(dt.timestamp(startDate)) * 1000

end = start_date - end_date

#BTC 가격
binance = ccxt.binance()
ohlcvs = binance.fetch_ohlcv('BTC/USDT', timeframe='1d', since=startDate, limit=100)

for idx, ohlcv in enumerate(ohlcvs):
    ohlcvs[idx] = [dt.fromtimestamp(ohlcv[0]/1000).strftime('%Y-%m-%d %H:%M:%S'), ohlcv[1], ohlcv[2], ohlcv[3], ohlcv[4],ohlcv[5]]

df_btc = pd.DataFrame(ohlcvs)
df_btc.columns = ['Time', 'Open','High','Low','Close','Volume']
df_btc['Time'] = pd.to_datetime(df_btc['Time'], format='%Y-%m-%d %H:%M:%S', errors='raise')
df_btc = df_btc[df_btc['Time'] >= '2021-06-24'].reset_index(drop = True)
df_btc.set_index('Time',inplace=True)



bt = Backtest(df_btc, SmaCross, cash=100_000, commission=.002)
stats = bt.run()

result = bt.plot(filename='./result/backtesting_image',open_browser=False)

st.subheader(f'백테스팅 결과')
st.bokeh_chart(result)


