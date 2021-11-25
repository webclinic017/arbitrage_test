import streamlit as st
import datetime
from utils import data_crawler
from utils import template
from utils import simulation

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
#BactTesting
#--------------------------------------------------

simulation.bactest(Selectbox,Selectbox_compare,klay_count,commission_fee,df_btc,df_klay)

# st.dataframe(stats_btc.style.format({"E": "{:.2f}"}),width=1000,height=500)
    

