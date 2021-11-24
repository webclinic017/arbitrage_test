from backtesting import Strategy
from backtesting.lib import crossover
import pandas as pd

def SMA(values, n):
    """
    Return simple moving average of `values`, at
    each step taking into account `n` previous values.
    """
    return pd.Series(values).rolling(n).mean()



class SmaCross(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    n1 = 10
    n2 = 20
    
    def init(self):
        # Precompute the two moving averages
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)
    
    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if crossover(self.sma1, self.sma2):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif crossover(self.sma2, self.sma1):
            self.position.close()
            self.sell()

def Original(df_klay,df_btc) :
    net = []

    #리밸런스 1일
    balance_1 = 0
    for i in range(0,113,1) :

        balance_1 += df_klay.iloc[i].Close * 10 / df_btc.iloc[i].Close
        net.append([df_klay.iloc[i].name, df_klay.iloc[i].Close, 1,balance_1])

    #리밸런스 14일
    balance_14 = 0
    for i in range(0,len(df_klay),14) :
        balance_14 += df_klay.iloc[i].Close * 140 / df_btc.iloc[i].Close
        net.append([df_klay.iloc[i].name, df_klay.iloc[i].Close, 14,balance_14])

    return net

def abcd_strategy(df_klay,df_btc) :
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
    commission_fee = 0.05
    u=0.03
    l=0.03

    for i in range(len(df_btc)):
        today_klay = df_klay.iloc[i]
        today_btc = df_btc.iloc[i]
        klay += 100

        # Sell_klay
        if (today_klay.Close > today_klay.MA_21) and (abs(1 - today_klay.upper_band / today_klay.Close) < l):
            if klay > 0:
                money += klay * today_klay.Close * commission_fee
                klay = 0
                net.append([today_klay.Time, today_klay.Close, 0, money])

                
        # Buy_btc
        if (today_btc.Close < today_btc.MA_21) and (abs(1 - today_btc.Close / today_btc.lower_band) < u):
            if money > 0:
                btc += money / today_btc.Close
                money = 0
                net.append([today_btc.Time, today_btc.Close, 1, btc])

    return net