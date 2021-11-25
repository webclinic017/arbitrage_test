import matplotlib.pyplot as plt
import matplotlib.dates as dates
import streamlit as st
import matplotlib
import numpy as np
from utils.Alpha_Function import Original
from utils.Alpha_Function import abcd_strategy
from utils import template


def bactest(Selectbox,Selectbox_compare,klay_count,commission_fee,df_btc,df_klay) :
    st.subheader(f'백테스팅 결과')

    if Selectbox == 'ABCD_Strategy' :
        net1 = abcd_strategy(klay_count,commission_fee,df_klay,df_btc)
        
    if Selectbox_compare == 'Original' :
        net = Original(klay_count,commission_fee,df_klay,df_btc)
            
    test_result = trading_history(Selectbox,Selectbox_compare,df_klay,df_btc,net,net1)
    st.pyplot(test_result)

def trading_history(Selectbox,Selectbox_compare,stock,stock1,net,net1, std=2):
    
    #set plot
    matplotlib.rcParams.update({'font.size': 22})
    fig = plt.figure(figsize=(20,40))
    plt.style.use('seaborn-whitegrid')
    plt.xlim([stock.index.min(), stock.index.max()])

    top_axes = plt.subplot2grid((6,4), (0,0), rowspan=3, colspan=4)
    bottom_axes2 = plt.subplot2grid((6,4), (3,0), rowspan=1, colspan=4, sharex=top_axes)
    bottom_axes1 = plt.subplot2grid((6,4), (4,0), rowspan=1, colspan=4, sharex=top_axes)
    bottom_axes = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex=top_axes)   

    # set top plot
    top_axes.plot(stock.index, stock.Close, color='#3388cf', label='KLAY_Price',linewidth=7.0)
    top_axes.set_ylabel('KLAY_Price',color='#3388cf')
    top_axes1 = top_axes.twinx()
    top_axes1.set_ylabel('BTC_Price', color='#ffa33f')
    top_axes1.plot(stock1.index, stock1.Close, color='#ffa33f', label='BTC_Price',linewidth=7.0)

    for i,j in zip(net,net1):
        
            if j[2] == 'btc' :
                color = '#ff005e'
                top_axes1.plot_date(j[0], j[1], color=color,markersize = 20)

            if j[2] == 'money' :
                color = 'darkcyan'
                top_axes.plot_date(j[0], j[1], color=color,markersize = 20)        



    top_axes1.plot_date([],[],label='BTC_Buy', c='#ff005e')
    top_axes1.plot_date([],[],label='Klay_Sell', c='darkcyan')

    lines, labels = top_axes.get_legend_handles_labels()
    lines2, labels2 = top_axes1.get_legend_handles_labels()
    top_axes1.legend(lines + lines2, labels + labels2,ncol=1, loc=2,frameon=True, borderpad=.6, prop={'size': 20})
    
    # set bottom2 plot
    Klay_Time1 = [i[0] for i in net if i[2] != 'btc']
    Klay_Equity1 = [i[3] for i in net if i[2] != 'btc']   
    Klay_Time2 = [i[0] for i in net1 if i[2] != 'btc']
    Klay_Equity2 = [i[3] for i in net1 if i[2] != 'btc']


    bottom_axes2.set_ylabel('Klay_Equity', color='#ffa33f')
    bottom_axes2.plot_date(Klay_Time1, Klay_Equity1,linestyle='-', fmt='#ff005e',marker='',label= Selectbox_compare ,linewidth=7.0)
    bottom_axes2.plot_date(Klay_Time2, Klay_Equity2,linestyle='-', fmt='darkcyan',marker='',label= Selectbox ,linewidth=7.0)
    bottom_axes2.plot_date([], [],linestyle='-')
    bottom_axes2.legend(ncol=1,loc=2,frameon=True,fontsize=10, borderpad=.6, prop={'size': 20})
    
    # set bottom1 plot
    Money_Time1 = [i[0] for i in net if i[2] != 'klay']
    Money_Equity1 = [i[3] for i in net if i[2] != 'klay']   
    Money_Time2 = [i[0] for i in net1 if i[2] != 'klay']
    Money_Equity2 = [i[3] for i in net1 if i[2] != 'klay']


    bottom_axes1.set_ylabel('Money_Equity', color='#ffa33f')
    bottom_axes1.plot_date(Money_Time1, Money_Equity1,linestyle='-', fmt='#ff005e',marker='',label= Selectbox_compare ,linewidth=7.0)
    bottom_axes1.plot_date(Money_Time2, Money_Equity2,linestyle='-', fmt='darkcyan',marker='',label= Selectbox ,linewidth=7.0)
    bottom_axes1.plot_date([], [],linestyle='-')
    bottom_axes1.legend(ncol=1,loc=2,frameon=True,fontsize=10, borderpad=.6, prop={'size': 20})

    # set bottom plot

    BTC_Time1 = [i[0] for i in net if i[2] == 'btc']
    BTC_Time2 = [i[0] for i in net1 if i[2] == 'btc']
    BTC_Equity1 = [i[3] for i in net if i[2] == 'btc']
    BTC_Equity2 = [i[3] for i in net1 if i[2] == 'btc']

    bottom_axes.set_ylabel('BTC_Equity', color='#ffa33f')
    bottom_axes.plot_date(BTC_Time1, BTC_Equity1,linestyle='-', fmt='#ff005e',marker='',label=Selectbox_compare,linewidth=7.0)
    bottom_axes.plot_date(BTC_Time2, BTC_Equity2,linestyle='-', fmt='darkcyan',marker='',label= Selectbox ,linewidth=7.0)
    bottom_axes.plot_date([], [],linestyle='-')
    bottom_axes.legend(ncol=1,loc=2,frameon=True,fontsize=10, borderpad=.6, prop={'size': 20})
    bottom_axes.xaxis.set_major_locator(dates.MonthLocator())

    return fig

    