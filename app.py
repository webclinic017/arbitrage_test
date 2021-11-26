import streamlit as st
import datetime
from utils import data_crawler
from utils import template
from utils import simulation
from utils.Alpha_Function import Run_Algo

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Set Template
#--------------------------------------------------
startDate, end, klay_count,Selectbox,Selectbox_compare,commission_fee = template.Template()
    
#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Data input
#--------------------------------------------------
df_klay = data_crawler.klay(startDate,end)
df_btc = data_crawler.btc(startDate,end)

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Run Algorithm
#--------------------------------------------------
net,net1 = Run_Algo(Selectbox,Selectbox_compare,klay_count,commission_fee,df_btc,df_klay)

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#BactTesting
#--------------------------------------------------
simulation.trading_history(Selectbox,Selectbox_compare,df_klay,df_btc,net,net1)

