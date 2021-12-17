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

def Template(df) :
    
    #~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-
    # Set page-config
    #--------------------------------------------------
    st.set_page_config(page_title="BTC_Trade",page_icon=":chart_with_upwards_trend:", layout="centered", initial_sidebar_state='expanded')
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

    with st.sidebar.form(key="운용기간"):
        st.markdown("**운용기간**")
        start_date = st.date_input("시작일", datetime.date.today() - datetime.timedelta(days=100),help = '`Select` start_date to get started 😏')
        end_date = st.date_input("종료일", datetime.date.today(),help = '`Select` end_date to get started 😏')
        
        st.markdown("**운용할 총 BTC갯수**")
        total_BTC = st.number_input("기간동안 사용할 BTC 갯수",
                value=10000,
                min_value=1000,
                help = '기간동안 사용할 `BTC` 갯수 😏')
        
        st.markdown("**수수료**")
        commission_fee = st.number_input("거래소 수수료 계산",
                value=0.05,
                help = '수수료')
        
        st.form_submit_button("Run")


    st.sidebar.subheader('**비교할 전략 선택**')
    Category_compare = df['Category'].unique()
    Category_compare_choice = st.sidebar.selectbox("Select Category", Category_compare,key="Category_compare")
    Strategy_compare_option = df[(df['Category'] == Category_compare_choice)]
    Selectbox_compare = st.sidebar.selectbox(
                                    "Select Strategy",
                                    options=Strategy_compare_option,
                                    key="Selectbox_compare",
                                    help="`Select` One Of The Strategy 😏"

                                )

    st.sidebar.subheader('**테스트할 전략 선택**')
    Category = df['Category'].unique()
    Category_choice = st.sidebar.selectbox("Select Category", Category,key="Category")   
    Strategy_option = df[(df['Category'] == Category_choice)]
    Selectbox = st.sidebar.selectbox(
                                "Select Strategy",
                                options=Strategy_option[::-1],
                                key="Selectbox",
                                help="`Select` One Of The Strategy 😏"
                            )

    startDate = dt.strptime(str(start_date), "%Y-%m-%d")
    endDate = dt.strptime(str(end_date), "%Y-%m-%d")
    
    return startDate, endDate, total_BTC , 1-commission_fee,Category_choice,Category_compare_choice,Selectbox,Selectbox_compare
