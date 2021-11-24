from backtesting import Backtest
from utils.Alpha_Function import SmaCross
from utils.Alpha_Function import Original
from utils.Alpha_Function import abcd_strategy
from utils import template
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import streamlit as st

def bactest(Selectbox,df_btc,df_klay) :
    st.subheader(f'백테스팅 결과')
    if Selectbox == 'SMA_CROSS' :
        bt = Backtest(df_btc, SmaCross, cash=100_000, commission=.002)
        stats = bt.run()
        stats_df = template.stats_df(stats)
        result = bt.plot(filename='./asset/backtesting_result',open_browser=False)
        st.bokeh_chart(result)
        st.dataframe(stats_df.style.format({"E": "{:.2f}"}),width=1000,height=500)

    if Selectbox == 'ABCD_Strategy' :
        net = Original(df_klay,df_btc)
        net1 = abcd_strategy(df_klay,df_btc)
        test_result = trading_history3(df_klay,df_btc,net,net1)
        st.pyplot(test_result)

def trading_history3(stock,stock1,net,net1, std=2): 
    fig = plt.figure(figsize=(20,10))
    plt.style.use('seaborn-whitegrid')

    top_axes = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
    bottom_axes = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4, sharex=top_axes)

    top_axes.plot(stock.index, stock.Close, color='#3388cf', label='KLAY_Price')
    top_axes.set_ylabel('KLAY_Price',color='#3388cf')
    top_axes1 = top_axes.twinx()  
    top_axes1.set_ylabel('BTC_Price', color='#ffa33f')
    bottom_axes.set_ylabel('BTC_Equity', color='#ffa33f')
    top_axes1.plot(stock1.index, stock1.Close, color='#ffa33f', label='BTC_Price')

    for i,j in zip(net,net1):
            # if i[2] == 1:
            #     color = '#ff005e'
            #     top_axes.plot_date(i[0], i[1], color=color)


            if i[2] == 14 :
                color = 'darkcyan'
                top_axes.plot_date(i[0], i[1], color=color)

            if j[2] == 1 :
                color = '#ff005e'
                top_axes1.plot_date(j[0], j[1], color=color)

            if j[2] == 0 :
                color = 'darkcyan'
                top_axes.plot_date(j[0], j[1], color=color)        


    Time1 = [i[0] for i in net if i[2] == 14]
    Time2 = [i[0] for i in net1 if i[2] == 1]
    Equity1 = [i[3] for i in net if i[2] == 14]
    Equity2 = [i[3] for i in net1 if i[2] == 1]
    bottom_axes.plot_date(Time1, Equity1,linestyle='-', fmt='#ff005e',marker='',label='Original')
    bottom_axes.plot_date(Time2, Equity2,linestyle='-', fmt='darkcyan',marker='',label='Algo')

    top_axes1.plot_date([],[],label='BTC_Buy', c='#ff005e')
    top_axes1.plot_date([],[],label='Klay_Sell', c='darkcyan')
    top_axes1.xaxis.set_major_locator(dates.MonthLocator())
    bottom_axes.plot_date([], [],linestyle='-')
    lines, labels = top_axes.get_legend_handles_labels()
    lines2, labels2 = top_axes1.get_legend_handles_labels()
    top_axes1.legend(lines + lines2, labels + labels2,ncol=1, loc=2,frameon=True, borderpad=.6)
    bottom_axes.legend(ncol=1,loc=2,frameon=True,fontsize=10, borderpad=.6)

    # top_axes1.get_yaxis().set_visible(False)
    plt.xlim([stock.index.min(), stock.index.max()])

    return fig
