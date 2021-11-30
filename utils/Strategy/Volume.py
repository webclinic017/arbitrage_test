import pandas as pd
import numpy as np
import pandas_ta as ta

def Run(Selectbox,klay_count,commission_fee,df_btc,df_klay) :
    
    net = globals()[Selectbox](klay_count,commission_fee,df_klay,df_btc)        
    
    return net