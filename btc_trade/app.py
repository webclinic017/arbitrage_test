import streamlit as st
from utils import Strategy_list
from utils import data_crawler
from utils import template
from utils import simulation
from utils.Strategy import TestStrategy
from utils.Portfolio_Function import Portfolio

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Set Strategy_list
#--------------------------------------------------
Strategy_list = Strategy_list.get_Strategy_list()

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Set Template
#--------------------------------------------------
startDate, endDate, total_BTC,commission_fee,Category_choice,Category_compare_choice,Selectbox,Selectbox_compare = template.Template(Strategy_list)
    
#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Data input
#--------------------------------------------------
df_btc = data_crawler.btc(startDate,endDate)

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Run Algorithm
#--------------------------------------------------





# #~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
# #BactTesting
# #--------------------------------------------------
st.subheader(f'백테스팅 결과')
fig = simulation.trading_history(Selectbox,Selectbox_compare,df_klay,df_btc,net1,net2)
st.pyplot(fig)
