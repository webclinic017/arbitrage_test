import pandas as pd
import numpy as np
import pandas_ta as ta

def Run(Selectbox,klay_count,commission_fee,df_btc,df_klay) :
    
    net = globals()[Selectbox](klay_count,commission_fee,df_klay,df_btc)        

    
    return net

def Rebalance14_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    
    def signal(df) :
        signals = pd.DataFrame()
        signals['Close'] = df_btc['Close']
        signals['signal'] = -1
        signals = signals.reset_index()
        signals.loc[(signals.index % 14 == 0) ,'signal'] = 1
        return list(signals['signal'])

    #리밸런스 14일
    signal_btc = signal(df_btc)
    signal_klay = signal(df_klay)
    klay = 0
    money = 0
    btc = 0
    net = []

    for i in range(len(df_btc)):
      today_klay = df_klay.iloc[i]
      today_btc = df_btc.iloc[i]
      Sell_signal = signal_klay[i]
      Buy_signal = signal_btc[i]
      klay += klay_count
      net.append([today_klay.name, today_klay.Close, 'klay', klay])

      # Sell_klay
      if Sell_signal == -1:
        if klay > 0:
              money += klay * today_klay.Close * commission_fee
              net.append([today_klay.name, today_klay.Close, 'money', money])
              klay = 0

      # Buy_btc
      if Buy_signal == 1:
        if money > 0:
              btc += money / today_btc.Close * commission_fee
              net.append([today_btc.name, today_btc.Close, 'btc', btc])
              money = 0

    return net