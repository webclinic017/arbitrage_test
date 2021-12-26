from utils.Strategy import TestStrategy,Candles
import pandas as pd

def get_Strategy_list() :

    Name = 'Strategy'
    Strategy = [prop for prop in dir(TestStrategy) if '_Strategy' in prop]
    df_TestStrategy = pd.DataFrame(Strategy, columns=[Name])
    df_TestStrategy['Category'] = 'TestStrategy'

    Name = 'Strategy'
    Strategy = [prop for prop in dir(Candles) if '_Strategy' in prop]
    df_Candles = pd.DataFrame(Strategy, columns=[Name])
    df_Candles['Category'] = 'Candles'

    df = pd.concat([df_TestStrategy,df_Candles])

    return df




