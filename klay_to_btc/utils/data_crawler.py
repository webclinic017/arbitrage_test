from datetime import datetime as dt
import pandas as pd
from messari.messari import Messari
messari = Messari('7c415011-ef64-467b-b3b6-bba85e6e2136')

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#BTC 가격
#--------------------------------------------------

def btc(startDate,endDate, messari = messari) :
    assets = 'btc'
    metric = 'price'
    df_btc = messari.get_metric_timeseries(asset_slugs=assets, asset_metric=metric, start=startDate, end=endDate)
    df_btc.columns = df_btc.columns.get_level_values(1)
    df_btc = df_btc.reset_index()
    df_btc.columns = ['Time', 'Open','High','Low','Close','Volume']
    df_btc.set_index('Time',inplace=True)

    return df_btc

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#KLAY 가격
#--------------------------------------------------

def klay(startDate,endDate, messari = messari) :
    assets = 'klay'
    metric = 'price'
    df_klay = messari.get_metric_timeseries(asset_slugs=assets, asset_metric=metric, start=startDate, end=endDate)
    df_klay.columns = df_klay.columns.get_level_values(1)
    df_klay = df_klay.reset_index()
    df_klay.columns = ['Time', 'Open','High','Low','Close','Volume']
    df_klay.set_index('Time',inplace=True)

    return df_klay

