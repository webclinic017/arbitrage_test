import pandas as pd
import numpy as np
import pandas_ta as ta

def Run_Algo(Selectbox,Selectbox_compare,klay_count,commission_fee,df_btc,df_klay) :
    
    # 비교할 알고리즘 
    net1 = globals()[Selectbox_compare](klay_count,commission_fee,df_klay,df_btc)        
    # 테스트할 알고리즘
    net2 = globals()[Selectbox](klay_count,commission_fee,df_klay,df_btc)
    
    return net1, net2

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

# def ABCD_Strategy(klay_count,commission_fee,df_klay,df_btc) :
#     def signal(df) :
#         u=0.03
#         l=0.0
#         rolling_mean = df.Close.rolling(21).mean()
#         rolling_std = df.Close.rolling(21).std()
#         signals = pd.DataFrame(index=df.index)
#         signals['Close'] = df['Close']
#         signals['signal'] = 0.0
#         signals['upper_band'] = rolling_mean + (rolling_std*2)
#         signals['lower_band'] = rolling_mean - (rolling_std*2)
#         signals['MA_21'] = signals['Close'].rolling(21).mean().shift()
#         signals.loc[(signals.Close > signals.MA_21) & (abs(1 - signals.upper_band / signals.Close) < l) , 'signal'] = -1
#         signals.loc[(signals.Close < signals.MA_21) & (abs(1 - signals.Close / signals.lower_band) < u), 'signal'] = 1

#         return list(signals['signal'])

#     signal_btc = signal(df_btc)
#     signal_klay = signal(df_klay)
#     klay = 0
#     money = 0
#     btc = 0
#     net = []

#     for i in range(len(df_btc)):
#       today_klay = df_klay.iloc[i]
#       today_btc = df_btc.iloc[i]
#       Sell_signal = signal_klay[i]
#       Buy_signal = signal_btc[i]
#       klay += klay_count
#       net.append([today_klay.name, today_klay.Close, 'klay', klay])

#       # Sell_klay
#       if Sell_signal == -1:
#         if klay > 0:
#               money += klay * today_klay.Close * commission_fee
#               net.append([today_klay.name, today_klay.Close, 'money', money])
#               klay = 0

#       # Buy_btc
#       if Buy_signal == 1:
#         if money > 0:
#               btc += money / today_btc.Close * commission_fee
#               net.append([today_btc.name, today_btc.Close, 'btc', btc])
#               money = 0

#     return net

# def Turtle_Strategy(klay_count,commission_fee,df_klay,df_btc) :
#     def signal(df) :
#         count = int(np.ceil(len(df) * 0.1))
#         signals = pd.DataFrame(index=df.index)
#         signals['signal'] = 0.0
#         signals['trend'] = df['Close']
#         signals['RollingMax'] = (signals.trend.shift(1).rolling(count).max())
#         signals['RollingMin'] = (signals.trend.shift(1).rolling(count).min())
#         signals.loc[signals['RollingMax'] < signals.trend, 'signal'] = -1
#         signals.loc[signals['RollingMin'] > signals.trend, 'signal'] = 1
#         signals
#         return list(signals['signal']) 

#     signal_klay = signal(df_klay)
#     signal_btc = signal(df_btc)

#     klay = 0
#     money = 0
#     btc = 0
#     net = []
    
#     for i in range(len(df_btc)):
#         today_klay = df_klay.iloc[i]
#         today_btc = df_btc.iloc[i]
#         Sell_signal = signal_klay[i]
#         Buy_signal = signal_btc[i]
#         klay += klay_count
#         net.append([today_klay.name, today_klay.Close, 'klay', klay])

#         # Sell_klay
#         if Sell_signal == -1:
#           if klay > 0:
#                 money += klay * today_klay.Close * commission_fee
#                 net.append([today_klay.name, today_klay.Close, 'money', money])
#                 klay = 0

#         # Buy_btc
#         if Buy_signal == 1:
#           if money > 0:
#                 btc += money / today_btc.Close * commission_fee
#                 net.append([today_btc.name, today_btc.Close, 'btc', btc])
#                 money = 0

#     return net

# def moving_average_Strategy(klay_count,commission_fee,df_klay,df_btc) :

#     # 10일 이동평균선이 20일 이동평균선 위에 있을때 사고 아님 팔고
#     def signal(df) :
#         short_window = 10
#         long_window = 20

#         signals = pd.DataFrame(index=df.index)
#         signals['signal'] = 0.0

#         signals['short_ma'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
#         signals['long_ma'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

#         signals['signal'][short_window:] = np.where(signals['short_ma'][short_window:] 
#                                                     > signals['long_ma'][short_window:], 1.0, 0.0)   
#         signals['positions'] = signals['signal'].diff()
#         return list(signals['signal'])

#     signal_klay = signal(df_klay)
#     signal_btc = signal(df_btc)

#     klay = 0
#     money = 0
#     btc = 0
#     net = []

#     for i in range(len(df_btc)):
#         today_klay = df_klay.iloc[i]
#         today_btc = df_btc.iloc[i]
#         Sell_signal = signal_klay[i]
#         Buy_signal = signal_btc[i]
#         klay += klay_count
#         net.append([today_klay.name, today_klay.Close, 'klay', klay])

#         # Sell_klay
#         if Sell_signal == -1:
#           if klay > 0:
#                 money += klay * today_klay.Close * commission_fee
#                 net.append([today_klay.name, today_klay.Close, 'money', money])
#                 klay = 0

#         # Buy_btc
#         if Buy_signal == 1:
#           if money > 0:
#                 btc += money / today_btc.Close * commission_fee
#                 net.append([today_btc.name, today_btc.Close, 'btc', btc])
#                 money = 0
#     return net

# def RSI21_Strategy(klay_count,commission_fee,df_klay,df_btc) :
#     def signal(df) :
#         rsi = df.ta.rsi(length = 21,append=True)
#         RSIoverSold = 50
#         RSIoverBought = 50
#         signals = pd.DataFrame(index=df.index)
#         signals['signal'] = 0.0
#         signals['RSI_21'] = df['RSI_21']
#         signals.loc[signals.RSI_21 > RSIoverBought, 'signal'] = -1
#         signals.loc[signals.RSI_21 < RSIoverSold , 'signal'] = 1
#         signals
#         return list(signals['signal']) 

#     signal_klay = signal(df_klay)
#     signal_btc = signal(df_btc)

#     klay = 0
#     money = 0
#     btc = 0
#     net = []
    
#     for i in range(len(df_btc)):
#         today_klay = df_klay.iloc[i]
#         today_btc = df_btc.iloc[i]
#         Sell_signal = signal_klay[i]
#         Buy_signal = signal_btc[i]
#         klay += klay_count
#         net.append([today_klay.name, today_klay.Close, 'klay', klay])

#         # Sell_klay
#         if Sell_signal == -1:
#           if klay > 0:
#                 money += klay * today_klay.Close * commission_fee
#                 net.append([today_klay.name, today_klay.Close, 'money', money])
#                 klay = 0

#         # Buy_btc
#         if Buy_signal == 1:
#           if money > 0:
#                 btc += money / today_btc.Close * commission_fee
#                 net.append([today_btc.name, today_btc.Close, 'btc', btc])
#                 money = 0

#     return net


# def SuperTrend_Strategy(klay_count,commission_fee,df_klay,df_btc) :
#     def signal(df) :
#         df = df.ta.cdl_pattern(name="supertrend")
#         return list(df['SUPERTd_7_3.0'])

#     signal_klay = signal(df_klay)
#     signal_btc = signal(df_btc)

#     klay = 0
#     money = 0
#     btc = 0
#     net = []
    
#     for i in range(len(df_btc)):
#         today_klay = df_klay.iloc[i]
#         today_btc = df_btc.iloc[i]
#         Sell_signal = signal_klay[i]
#         Buy_signal = signal_btc[i]
#         klay += klay_count
#         net.append([today_klay.name, today_klay.Close, 'klay', klay])

#         # Sell_klay
#         if Sell_signal == -1:
#           if klay > 0:
#                 money += klay * today_klay.Close * commission_fee
#                 net.append([today_klay.name, today_klay.Close, 'money', money])
#                 klay = 0

#         # Buy_btc
#         if Buy_signal == 1:
#           if money > 0:
#                 btc += money / today_btc.Close * commission_fee
#                 net.append([today_btc.name, today_btc.Close, 'btc', btc])
#                 money = 0

#     return net

def Shootingstar_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        df = df.ta.cdl_pattern(name="shootingstar")
        return list(df['CDL_SHOOTINGSTAR'])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

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