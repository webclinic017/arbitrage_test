from backtesting import Backtest
from utils.Alpha_Function import SmaCross
from utils import template

def bactest(Selectbox,df_btc) :
    if Selectbox == 'SMA_CROSS' :
        bt = Backtest(df_btc, SmaCross, cash=100_000, commission=.002)
        stats = bt.run()
        result = bt.plot(filename='./asset/backtesting_result',open_browser=False)
        stats_df = template.stats_df(stats)
        return stats_df, result
    else : return False, False