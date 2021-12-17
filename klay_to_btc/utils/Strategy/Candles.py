import pandas as pd
import numpy as np
import pandas_ta as ta

def Run(Selectbox,df_btc,df_klay) :
    
    signal_klay,signal_btc = globals()[Selectbox](df_klay,df_btc)        
    
    return signal_klay,signal_btc

def Shootingstar_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="shootingstar")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def doji_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="doji")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def longleggeddoji_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="longleggeddoji")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def hammer_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="hammer")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def dojistar_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="dojistar")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def takuri_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="takuri")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def inside_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="inside")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def rickshawman_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="rickshawman")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def longline_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="longline")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def stalledpattern_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="stalledpattern")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def advanceblock_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="advanceblock")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def hikkake_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="hikkake")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def shortline_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="shortline")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def matchinglow_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="matchinglow")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def highwave_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="highwave")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def spinningtop_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="spinningtop")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def marubozu_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="marubozu")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def belthold_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="belthold")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def closingmarubozu_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="closingmarubozu")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def engulfing_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="engulfing")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def dragonflydoji_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="dragonflydoji")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def gravestonedoji_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="gravestonedoji")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def harami_Strategy(df_klay,df_btc) :
    def signal(df) :
        signal = df.ta.cdl_pattern(name="harami")
        return list(signal.iloc[:, 0])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc