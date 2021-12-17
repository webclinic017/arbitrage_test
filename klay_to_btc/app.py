import streamlit as st
from utils import Strategy_list
from utils import data_crawler
from utils import template
from utils import simulation
from utils.Strategy import Candles,Etc,Momentum,Overlap,Statistics,Trend,Volatility,Volume
from utils.Portfolio_Function import Portfolio

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Set Strategy_list
#--------------------------------------------------
Strategy_list = Strategy_list.get_Strategy_list()

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Set Template
#--------------------------------------------------
startDate, endDate, total_klay, klay_count,commission_fee,Category_choice,Category_compare_choice,Selectbox,Selectbox_compare = template.Template(Strategy_list)
    
#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Data input
#--------------------------------------------------
df_klay = data_crawler.klay(startDate,endDate)
df_btc = data_crawler.btc(startDate,endDate)

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Run Algorithm
#--------------------------------------------------

methods = {'Candles': Candles.Run, 'Etc': Etc.Run, 'Momentum': Momentum.Run, 'Overlap': Overlap.Run, 'Statistics': Statistics.Run, 'Trend': Trend.Run, 'Volatility': Volatility.Run, 'Volume': Volume.Run}

# 비교할 알고리즘 
if Category_compare_choice in methods:
    signal_klay1,signal_btc1 = methods[Category_compare_choice](Selectbox_compare,df_klay,df_btc)
    net1 = Portfolio(total_klay,klay_count,commission_fee,df_klay,df_btc,signal_klay1,signal_btc1)

if Category_choice in methods:
    signal_klay2,signal_btc2 = methods[Category_compare_choice](Selectbox_compare,df_klay,df_btc)
    net2 = Portfolio(total_klay,klay_count,commission_fee,df_klay,df_btc,signal_klay2,signal_btc2)



# #~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
# #BactTesting
# #--------------------------------------------------
st.subheader(f'백테스팅 결과')
fig = simulation.trading_history(Selectbox,Selectbox_compare,df_klay,df_btc,net1,net2)
st.pyplot(fig)
