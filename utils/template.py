import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import datetime as dt

def stats_df(stats) :
    stats_df = pd.DataFrame(stats)
    stats_df.iloc[0][0] = int(stats_df.iloc[0][0].date().strftime('%Y%m%d'))
    stats_df.iloc[1][0] = int(stats_df.iloc[1][0].date().strftime('%Y%m%d'))
    stats_df.iloc[2] = (stats_df.iloc[2] / np.timedelta64(1, 'D')).astype(int)
    stats_df.iloc[15] = (stats_df.iloc[15] / np.timedelta64(1, 'D')).astype(int)
    stats_df.iloc[16] = (stats_df.iloc[16] / np.timedelta64(1, 'D')).astype(int)
    stats_df.iloc[22] = (stats_df.iloc[22] / np.timedelta64(1, 'D')).astype(int)
    stats_df.iloc[23] = (stats_df.iloc[23] / np.timedelta64(1, 'D')).astype(int)
    stats_df = stats_df.iloc[:-3]
    stats_df.columns = ['value']
    
    return stats_df

def Template() :
    #~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
    # Set page-config
    #--------------------------------------------------
    st.set_page_config(page_title="AI_LAB",page_icon="📍", layout="centered", initial_sidebar_state='expanded')

    #~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
    # Set style
    #--------------------------------------------------
    st.markdown(
        """
        <style>
        .reportview-container {
            background: #EBECE5
        }
        a:link{ color:#325FE5; } 
        a:visited{ color:#325FE5; } 
        a:hover{ color:#325FE5; } 
        a:active{ color:#325FE5}
        </style>
        """,
        unsafe_allow_html=True
    )

    #~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
    # Title and Sub-title
    #--------------------------------------------------
    st.markdown(
        """
        <center>
            <h1>백테스팅 테스트</h1>
        </center>
        """,
        unsafe_allow_html=True
    )

    #~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
    # Sidebar Setup
    #--------------------------------------------------

    with st.sidebar.form(key="my_form1"):
        st.markdown("**운용기간**")
        start_date = st.date_input("시작일", datetime.date(2021, 7, 1),help = '`Select` start_date to get started 😏')
        end_date = st.date_input("종료일", datetime.date.today(),help = '`Select` end_date to get started 😏')

        st.markdown("**운용자금**")
        money = st.number_input("운용자금",
                value=100_000,
                min_value=100_000,
                help = '`Select` money to get started 😏')
        pressed1 = st.form_submit_button("Run")
        
    with st.sidebar.form(key="my_form2"):
        st.subheader('**알고리즘**')
        Selectbox = st.selectbox(
            "Select Algorithm",
            options=["SMA_CROSS", "en_beta", "al_beta", "pu_alpa"],
            help="Select One Of The Four options"
        )
        
        pressed2 = st.form_submit_button("Run")


    startDate = dt.strptime(str(start_date), "%Y-%m-%d")
    startDate = int(dt.timestamp(startDate)) * 1000
    end = (end_date - start_date).days
    if end > 1000 :
        end = 1000
    
    return startDate, end, money,Selectbox