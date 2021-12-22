from utils.Strategy import TestStrategy,TestStrategy2
import pandas as pd

def get_Strategy_list() :

    Name = 'Strategy'
    Strategy = [prop for prop in dir(TestStrategy) if '_Strategy' in prop]
    df_TestStrategy = pd.DataFrame(Strategy, columns=[Name])
    df_TestStrategy['Category'] = 'TestStrategy'

    Name = 'Strategy'
    Strategy = [prop for prop in dir(TestStrategy2) if '_Strategy' in prop]
    df_TestStrategy2 = pd.DataFrame(Strategy, columns=[Name])
    df_TestStrategy2['Category'] = 'TestStrategy2'

    df = pd.concat([df_TestStrategy,df_TestStrategy2])

    return df




