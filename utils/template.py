import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import datetime as dt
from utils.Strategy import Alpha_Function

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
    st.set_page_config(page_title="Klay_To_BTC",page_icon=":chart_with_upwards_trend:", layout="centered", initial_sidebar_state='expanded')
    option = [prop for prop in dir(Alpha_Function)if '_Strategy' in prop]
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
        start_date = st.date_input("시작일", datetime.date.today() - datetime.timedelta(days=100),help = '`Select` start_date to get started 😏')
        end_date = st.date_input("종료일", datetime.date.today(),help = '`Select` end_date to get started 😏')
        
        st.markdown("**운용Klay갯수**")
        klay_count = st.number_input("일일당 추가할 klay 갯수",
                value=100,
                min_value=10,
                help = '하루당 추가하는`klay` 갯수 😏')
        
        st.markdown("**수수료**")
        commission_fee = st.number_input("거래소 수수료 계산",
                value=0.05,
                help = '수수료')
        
        pressed1 = st.form_submit_button("Run")
        
    with st.sidebar.form(key="my_form2"):
        st.subheader('**비교할 전략**')
        Selectbox_compare = st.selectbox(
            "Select Strategy",
            options=option,
            help="`Select` One Of The Strategy 😏"
        )
        
        st.subheader('**테스트할 전략**')
        Selectbox = st.selectbox(
            "Select Strategy",
            options=option[::-1],
            help="`Select` One Of The Strategy 😏"
        )
        
        
        pressed2 = st.form_submit_button("Run")


    startDate = dt.strptime(str(start_date), "%Y-%m-%d")
    startDate = int(dt.timestamp(startDate)) * 1000
    end = (end_date - start_date).days
    if end > 1000 :
        end = 1000
    
    return startDate, end, klay_count,Selectbox,Selectbox_compare,commission_fee
