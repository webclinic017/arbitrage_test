
from utils.Strategy import Candles
from utils.Strategy import Etc
from utils.Strategy import Momentum
from utils.Strategy import Overlap
from utils.Strategy import Statistics
from utils.Strategy import Trend
from utils.Strategy import Volatility
from utils.Strategy import Volume
import pandas as pd

def get_Strategy_list() :

    Name = 'Strategy'
    Strategy = [prop for prop in dir(Candles) if '_Strategy' in prop]
    df_Candles = pd.DataFrame(Strategy, columns=[Name])
    df_Candles['Category'] = 'Candles'

    Name = 'Strategy'
    Strategy = [prop for prop in dir(Etc) if '_Strategy' in prop]
    df_Etc = pd.DataFrame(Strategy, columns=[Name])
    df_Etc['Category'] = 'Etc'

    Name = 'Strategy'
    Strategy = [prop for prop in dir(Momentum) if '_Strategy' in prop]
    df_Momentum = pd.DataFrame(Strategy, columns=[Name])
    df_Momentum['Category'] = 'Momentum'

    Name = 'Strategy'
    Strategy = [prop for prop in dir(Overlap) if '_Strategy' in prop]
    df_Overlap = pd.DataFrame(Strategy, columns=[Name])
    df_Overlap['Category'] = 'Overlap'

    Name = 'Strategy'
    Strategy = [prop for prop in dir(Statistics) if '_Strategy' in prop]
    df_Statistics = pd.DataFrame(Strategy, columns=[Name])
    df_Statistics['Category'] = 'Statistics'

    Name = 'Strategy'
    Strategy = [prop for prop in dir(Trend) if '_Strategy' in prop]
    df_Trend = pd.DataFrame(Strategy, columns=[Name])
    df_Trend['Category'] = 'Trend'

    Name = 'Strategy'
    Strategy = [prop for prop in dir(Volatility) if '_Strategy' in prop]
    df_Volatility = pd.DataFrame(Strategy, columns=[Name])
    df_Volatility['Category'] = 'Volatility'

    Name = 'Strategy'
    Strategy = [prop for prop in dir(Volume) if '_Strategy' in prop]
    df_Volume = pd.DataFrame(Strategy, columns=[Name])
    df_Volume['Category'] = 'Volume'

    df = pd.concat([df_Candles,df_Etc,df_Momentum,df_Overlap,df_Statistics,df_Trend,df_Volatility,df_Volume])

    return df




