import pandas as pd
import numpy as np
from talib import *

def Run(Selectbox,klay_count,commission_fee,df_btc,df_klay) :
    
    net = globals()[Selectbox](klay_count,commission_fee,df_klay,df_btc)        
    
    return net

def Shootingstar_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLSHOOTINGSTAR(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def doji_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = (df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def longleggeddoji_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLDOJI(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def hammer_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLHAMMER(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def dojistar_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLDOJISTAR(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def takuri_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLTAKURI(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def inside_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDL3INSIDE(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def rickshawman_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLRICKSHAWMAN(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def longline_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLLONGLINE(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def stalledpattern_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLSTALLEDPATTERN(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def advanceblock_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLADVANCEBLOCK(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def hikkake_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLHIKKAKE(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def shortline_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLSHORTLINE(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def matchinglow_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLMATCHINGLOW(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def highwave_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLHIGHWAVE(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def spinningtop_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLSPINNINGTOP(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def marubozu_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLMARUBOZU(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def belthold_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLBELTHOLD(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def closingmarubozu_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLCLOSINGMARUBOZU(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def engulfing_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLENGULFING(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def dragonflydoji_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLDRAGONFLYDOJI(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def gravestonedoji_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLGRAVESTONEDOJI(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net

def harami_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        signal = CDLHARAMI(df.Open,df.High,df.Low,df.Close)
        return list(signal)

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
        if Sell_signal < -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal > 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0

    return net