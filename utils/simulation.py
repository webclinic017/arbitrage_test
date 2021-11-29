import matplotlib.pyplot as plt
import matplotlib.dates as dates
import streamlit as st

def trading_history(Selectbox,Selectbox_compare,klay,btc,net,net2, std=2):
    st.subheader(f'백테스팅 결과')
    #set plot
    fig = plt.figure(figsize=(20,20))
    fig.patch.set_alpha(0.5)
    plt.style.use('seaborn-whitegrid')
    plt.xlim([klay.index.min(), klay.index.max()])
    plt.rcParams.update({'font.size': 22})
    plt.rcParams['axes.facecolor'] = '#EBECE5'

    top_axes = plt.subplot2grid((6,4), (0,0), rowspan=3, colspan=4)
    bottom_axes2 = plt.subplot2grid((6,4), (3,0), rowspan=1, colspan=4, sharex=top_axes)
    bottom_axes1 = plt.subplot2grid((6,4), (4,0), rowspan=1, colspan=4, sharex=top_axes)
    bottom_axes = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex=top_axes)   
    top_axes1 = top_axes.twinx()
    
    # set top plot
    top_axes.plot(klay.index, klay.Close, color='#3388cf', label='KLAY_Price',linewidth=7.0)
    top_axes.set_ylabel('KLAY_Price',color='#3388cf')
    top_axes1.set_ylabel('BTC_Price', color='#ffa33f')
    top_axes1.plot(btc.index, btc.Close, color='#ffa33f', label='BTC_Price',linewidth=7.0)

    for i,j in zip(net,net2):
        
            if j[2] == 'btc' :
                color = '#ff005e'
                top_axes1.plot_date(j[0], j[1], color=color,markersize = 20, alpha=0.7)

            if j[2] == 'money' :
                color = 'darkcyan'
                top_axes.plot_date(j[0], j[1], color=color,markersize = 20, alpha=0.7)        



    top_axes1.plot_date([],[],label='BTC_Buy', c='#ff005e',markersize = 20)
    top_axes1.plot_date([],[],label='Klay_Sell', c='darkcyan',markersize = 20)

    lines, labels = top_axes.get_legend_handles_labels()
    lines2, labels2 = top_axes1.get_legend_handles_labels()
    lgnd =top_axes1.legend(lines + lines2, labels + labels2,ncol=1, loc=2,frameon=True, borderpad=.6, prop={'size': 20})
    
    # set bottom2 plot
    Klay_Time1 = [i[0] for i in net if i[2] != 'btc']
    Klay_Equity1 = [i[3] for i in net if i[2] != 'btc']   
    Klay_Time2 = [i[0] for i in net2 if i[2] != 'btc']
    Klay_Equity2 = [i[3] for i in net2 if i[2] != 'btc']


    bottom_axes2.set_ylabel('Klay_Equity', color='#3388cf')
    bottom_axes2.plot_date(Klay_Time1, Klay_Equity1,linestyle='-', fmt='palegreen',marker='',label= Selectbox_compare ,linewidth=7.0)
    bottom_axes2.plot_date(Klay_Time2, Klay_Equity2,linestyle='-', fmt='darkcyan',marker='',label= Selectbox ,linewidth=7.0)
    bottom_axes2.plot_date([], [],linestyle='-')
    bottom_axes2.legend(ncol=1,loc=2,frameon=True,fontsize=10, borderpad=.6, prop={'size': 20})
    
    # set bottom1 plot
    Money_Time1 = [i[0] for i in net if i[2] != 'klay']
    Money_Equity1 = [i[3] for i in net if i[2] != 'klay']   
    Money_Time2 = [i[0] for i in net2 if i[2] != 'klay']
    Money_Equity2 = [i[3] for i in net2 if i[2] != 'klay']


    bottom_axes1.set_ylabel('Money_Equity', color='limegreen')
    bottom_axes1.plot_date(Money_Time1, Money_Equity1,linestyle='-', fmt='palegreen',marker='',label= Selectbox_compare ,linewidth=7.0)
    bottom_axes1.plot_date(Money_Time2, Money_Equity2,linestyle='-', fmt='darkcyan',marker='',label= Selectbox ,linewidth=7.0)
    bottom_axes1.plot_date([], [],linestyle='-')
    bottom_axes1.legend(ncol=1,loc=2,frameon=True,fontsize=10, borderpad=.6, prop={'size': 20})

    # set bottom plot

    BTC_Time1 = [i[0] for i in net if i[2] == 'btc']
    BTC_Time2 = [i[0] for i in net2 if i[2] == 'btc']
    BTC_Equity1 = [i[3] for i in net if i[2] == 'btc']
    BTC_Equity2 = [i[3] for i in net2 if i[2] == 'btc']

    bottom_axes.set_ylabel('BTC_Equity', color='#ffa33f')
    bottom_axes.plot_date(BTC_Time1, BTC_Equity1,linestyle='-', fmt='palegreen',marker='',label=Selectbox_compare,linewidth=7.0)
    bottom_axes.plot_date(BTC_Time2, BTC_Equity2,linestyle='-', fmt='darkcyan',marker='',label= Selectbox ,linewidth=7.0)
    bottom_axes.plot_date([], [],linestyle='-')
    bottom_axes.legend(ncol=1,loc=2,frameon=True,fontsize=10, borderpad=.6, prop={'size': 20})
    bottom_axes.xaxis.set_major_locator(dates.MonthLocator())

    st.pyplot(fig)


    