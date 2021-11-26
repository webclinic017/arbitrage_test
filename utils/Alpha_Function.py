import pandas as pd
import numpy as np

def Run_Algo(Selectbox,Selectbox_compare,klay_count,commission_fee,df_btc,df_klay) :
    
    # 비교할 알고리즘 
    net = globals()[Selectbox_compare](klay_count,commission_fee,df_klay,df_btc)        
    # 테스트할 알고리즘
    net1 = globals()[Selectbox](klay_count,commission_fee,df_klay,df_btc)
    
    return net, net1

def Original(klay_count,commission_fee,df_klay,df_btc) :
    net = []

    #리밸런싱 14일
    klay = 0
    btc = 0
    money = 0
    count = 0
    
    for i in range(0,len(df_klay)) :
        today_klay = df_klay.iloc[i]
        today_btc = df_btc.iloc[i]
        count += 1
        klay += klay_count
        net.append([today_klay.name, today_klay.Close, 'klay' ,klay])
        
        # Sell_klay
        if (count % 14) == 0 :
            money += klay * today_klay.Close * commission_fee
            net.append([today_klay.name, today_klay.Close, 'money' ,money])
            klay = 0
        
        # Buy_btc
        if (count % 14) == 0 :
            btc += money / today_btc.Close * commission_fee
            net.append([today_btc.name, today_btc.Close, 'btc' ,btc])
            money = 0
        
            
    return net

def ABCD_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def data(df) :
        rolling_mean = df.Close.rolling(21).mean()
        rolling_std = df.Close.rolling(21).std()
        df['upper_band'] = rolling_mean + (rolling_std*2)
        df['lower_band'] = rolling_mean - (rolling_std*2)
        df['MA_21'] = df['Close'].rolling(21).mean().shift()
        exp1 = df.Close.ewm(span=12, adjust=False).mean()
        exp2 = df.Close.ewm(span=26, adjust=False).mean()
        df['macd'] = exp1-exp2
        df['signal'] = df.macd.ewm(span=9, adjust=False).mean()
        df['Time'] = df.index
        df = df.reset_index(drop=True)

        return df

    df_btc = data(df_btc)
    df_klay = data(df_klay)

    klay = 0
    money = 0
    btc = 0
    net = []
    u=0.03
    l=0.03

    for i in range(len(df_btc)):
        today_klay = df_klay.iloc[i]
        today_btc = df_btc.iloc[i]
        klay += klay_count
        net.append([today_klay.Time, today_klay.Close, 'klay', klay])
        
        # Sell_klay
        if (today_klay.Close > today_klay.MA_21) and (abs(1 - today_klay.upper_band / today_klay.Close) < l):
            if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.Time, today_klay.Close, 'money', money])
                klay = 0

                
        # Buy_btc
        if (today_btc.Close < today_btc.MA_21) and (abs(1 - today_btc.Close / today_btc.lower_band) < u):
            if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.Time, today_btc.Close, 'btc', btc])
                money = 0
                
    return net

def Turtle_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        count = int(np.ceil(len(df) * 0.1))
        signals = pd.DataFrame(index=df.index)
        signals['signal'] = 0.0
        signals['trend'] = df['Close']
        signals['RollingMax'] = (signals.trend.shift(1).rolling(count).max())
        signals['RollingMin'] = (signals.trend.shift(1).rolling(count).min())
        signals.loc[signals['RollingMax'] < signals.trend, 'signal'] = -1
        signals.loc[signals['RollingMin'] > signals.trend, 'signal'] = 1
        signals
        return list(signals['signal']) 

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