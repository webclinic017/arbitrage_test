import warnings
warnings.filterwarnings('ignore')
import streamlit as st
from utils import Strategy_list
from utils import data_crawler
from utils import template
from utils.Strategy.TestStrategy import *
from utils.Strategy.Candles import *
import empyrical as ep
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Set Strategy_list
#--------------------------------------------------
Strategy_list = Strategy_list.get_Strategy_list()

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Set Template
#--------------------------------------------------
startDate, endDate, total_BTC,commission_fee,Category_choice,Selectbox = template.Template(Strategy_list)
    
#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Data input
#--------------------------------------------------
df_btc = data_crawler.btc(startDate,endDate)

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Run Strategy
#--------------------------------------------------
Strategy = globals()[Selectbox]

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Run Cerebro
#--------------------------------------------------
cerebro = bt.Cerebro()

## Add the Data Feed to Cerebro
data = df_btc
cerebro.adddata(data, name="ok")
cerebro.addstrategy(Strategy)

## Set our desired cash start
cerebro.broker.setcash(1000000)

## Add a FixedSize sizer according to the stake
cerebro.addsizer(bt.sizers.FixedSize, stake=5)
cerebro.addanalyzer(bt.analyzers.PyFolio,  _name='pyfolio')
## Set the commission
cerebro.broker.setcommission(commission=0.0)


# Run over everything
results = cerebro.run(maxcpus=1)  # [15]

# #~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
# #BactTesting
# #--------------------------------------------------

st.subheader(f'백테스팅 결과')

fig = cerebro.plot()[0][0]

st.pyplot(fig)


# dataframe

strat = results[0]
pyfoliozer = strat.analyzers.getbyname('pyfolio')
returns, positions, transactions, gross_lev = pyfoliozer.get_pf_items()

SIMPLE_STAT_FUNCS = [
    ep.annual_return,
    ep.cum_returns_final,
    ep.annual_volatility,
    ep.sharpe_ratio,
    ep.calmar_ratio,
    ep.stability_of_timeseries,
    ep.max_drawdown,
    ep.omega_ratio,
    ep.sortino_ratio,
    ep.tail_ratio,
]

STAT_FUNC_NAMES = {
    'annual_return': 'Annual return',
    'cum_returns_final': 'Cumulative returns',
    'annual_volatility': 'Annual volatility',
    'sharpe_ratio': 'Sharpe ratio',
    'calmar_ratio': 'Calmar ratio',
    'stability_of_timeseries': 'Stability',
    'max_drawdown': 'Max drawdown',
    'omega_ratio': 'Omega ratio',
    'sortino_ratio': 'Sortino ratio',
    'skew': 'Skew',
    'kurtosis': 'Kurtosis',
    'tail_ratio': 'Tail ratio',
    'common_sense_ratio': 'Common sense ratio',
    'value_at_risk': 'Daily value at risk',
    'alpha': 'Alpha',
    'beta': 'Beta',
}

stats = pd.Series()
for i,stat_func in enumerate(SIMPLE_STAT_FUNCS):
    stats[STAT_FUNC_NAMES[stat_func.__name__]] = stat_func(returns)
    stats.iloc[i] = str(np.round(stats.iloc[i]  * 100,3)) + '%'

perf_stats = pd.DataFrame(stats, columns=['Backtest'])
st.dataframe(perf_stats.astype(str),width= 1600, height= 1600)
