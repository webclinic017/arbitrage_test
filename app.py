import streamlit as st
from utils import Strategy_list
from utils import data_crawler
from utils import template
from utils import simulation
from utils.Strategy import Candles
from utils.Strategy import Etc
from utils.Strategy import Momentum
from utils.Strategy import Overlap
from utils.Strategy import Statistics
from utils.Strategy import Trend
from utils.Strategy import Volatility
from utils.Strategy import Volume

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Set Strategy_list
#--------------------------------------------------
Strategy_list = Strategy_list.get_Strategy_list()

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Set Template
#--------------------------------------------------
startDate, end, klay_count,commission_fee,Category_choice,Category_compare_choice,Selectbox,Selectbox_compare = template.Template(Strategy_list)
    
#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Data input
#--------------------------------------------------
df_klay = data_crawler.klay(startDate,end)
df_btc = data_crawler.btc(startDate,end)

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Run Algorithm
#--------------------------------------------------

methods = {'Candles': Candles.Run, 'Etc': Etc.Run, 'Momentum': Momentum.Run, 'Overlap': Overlap.Run, 'Statistics': Statistics.Run, 'Trend': Trend.Run, 'Volatility': Volatility.Run, 'Volume': Volume.Run}

# 비교할 알고리즘 
if Category_compare_choice in methods:
    net1 = methods[Category_compare_choice](Selectbox_compare,klay_count,commission_fee,df_btc,df_klay)

if Category_choice in methods:
    net2 = methods[Category_choice](Selectbox,klay_count,commission_fee,df_btc,df_klay)

# #~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
# #BactTesting
# #--------------------------------------------------
st.subheader(f'백테스팅 결과')
fig = simulation.trading_history(Selectbox,Selectbox_compare,df_klay,df_btc,net1,net2)
st.pyplot(fig)
