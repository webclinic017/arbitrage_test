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

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#KLAY 가격
#--------------------------------------------------

def klay(startDate,end) :
    binance = ccxt.binance()
    ohlcvs = binance.fetch_ohlcv('KLAY/USDT',  timeframe='1d', since=startDate, limit=end)

    for idx, ohlcv in enumerate(ohlcvs):
        ohlcvs[idx] = [dt.fromtimestamp(ohlcv[0]/1000).strftime('%Y-%m-%d %H:%M:%S'), ohlcv[1], ohlcv[2], ohlcv[3], ohlcv[4],ohlcv[5]]

    df_klay = pd.DataFrame(ohlcvs)
    df_klay.columns = ['Time', 'Open','High','Low','Close','Volume']
    df_klay['Time'] = pd.to_datetime(df_klay['Time'], format='%Y-%m-%d %H:%M:%S', errors='raise')
    df_klay.set_index('Time',inplace=True)
    return df_klay

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#XRP 가격
#--------------------------------------------------

def xrp(startDate,end) :
    binance = ccxt.binance()
    ohlcvs = binance.fetch_ohlcv('XRP/USDT',  '1d')

    for idx, ohlcv in enumerate(ohlcvs):
        ohlcvs[idx] = [dt.fromtimestamp(ohlcv[0]/1000).strftime('%Y-%m-%d %H:%M:%S'), ohlcv[1], ohlcv[2], ohlcv[3], ohlcv[4],ohlcv[5]]

    df_xrp = pd.DataFrame(ohlcvs)
    df_xrp.columns = ['Time', 'Open','High','Low','Close','Volume']
    df_xrp['Time'] = pd.to_datetime(df_xrp['Time'], format='%Y-%m-%d %H:%M:%S', errors='raise')
    df_xrp = df_xrp[df_xrp['Time'] >= '2021-06-24'].reset_index(drop = True)
    df_xrp.set_index('Time',inplace=True)
    return df_xrp

