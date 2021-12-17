import pandas as pd
import numpy as np
import pandas_ta as ta

def Run(Selectbox,df_klay,df_btc) :
    
    signal_klay,signal_btc = globals()[Selectbox](df_klay,df_btc)        
    
    return signal_klay,signal_btc

def Rebalance14_Strategy(df_klay,df_btc) :
    
    def signal(df) :
      signals = pd.DataFrame()
      signals['Close'] = df['Close']
      signals['signal'] = -1
      signals = signals.reset_index()
      signals.loc[(signals.index % 14 == 0) ,'signal'] = 1
      return list(signals['signal'])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc

def ebsw_Strategy(df_klay,df_btc) :

    def signal(df) :
      signal = df.ta.ebsw()
      return list(signal)
    
    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    return signal_klay, signal_btc
