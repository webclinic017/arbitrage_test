import streamlit as st
import datetime
from utils import data_crawler
from utils import template
from utils import simulation

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Set Template
#--------------------------------------------------
startDate, end, money,Selectbox = template.Template()
    
#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#Data input
#--------------------------------------------------
df_klay = data_crawler.klay(startDate,end)
df_btc = data_crawler.btc(startDate,end)

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
#BactTesting
#--------------------------------------------------

simulation.bactest(Selectbox,df_btc,df_klay)

# st.dataframe(stats_btc.style.format({"E": "{:.2f}"}),width=1000,height=500)
    

