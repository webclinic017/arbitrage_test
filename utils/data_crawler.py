import ccxt
from datetime import datetime as dt
import pandas as pd

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#BTC 가격
#--------------------------------------------------

def btc(startDate,end) :
    binance = ccxt.binance()
    ohlcvs = binance.fetch_ohlcv('BTC/USDT', timeframe='1d', since=startDate, limit=end)

    for idx, ohlcv in enumerate(ohlcvs):
        ohlcvs[idx] = [dt.fromtimestamp(ohlcv[0]/1000).strftime('%Y-%m-%d %H:%M:%S'), ohlcv[1], ohlcv[2], ohlcv[3], ohlcv[4],ohlcv[5]]

    df_btc = pd.DataFrame(ohlcvs)
    df_btc.columns = ['Time', 'Open','High','Low','Close','Volume']
    df_btc['Time'] = pd.to_datetime(df_btc['Time'], format='%Y-%m-%d %H:%M:%S', errors='raise')
    df_btc = df_btc[df_btc['Time'] >= '2021-06-24'].reset_index(drop = True)
    df_btc.set_index('Time',inplace=True)

    return df_btc