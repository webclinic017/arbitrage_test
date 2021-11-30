def moving_average_Strategy(klay_count,commission_fee,df_klay,df_btc) :

    # 10일 이동평균선이 20일 이동평균선 위에 있을때 사고 아님 팔고
    def signal(df) :
        short_window = 10
        long_window = 20

        signals = pd.DataFrame(index=df.index)
        signals['signal'] = 0.0

        signals['short_ma'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
        signals['long_ma'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

        signals['signal'][short_window:] = np.where(signals['short_ma'][short_window:] 
                                                    > signals['long_ma'][short_window:], 1.0, 0.0)   
        signals['positions'] = signals['signal'].diff()
        return list(signals['signal'])

    signal_klay = signal(df_klay)
    signal_btc = signal(df_btc)

    klay = 0
    money = 0
    btc = 0
    net = []

    for i in range(len(df_btc)):
        today_klay = df_klay.iloc[i]
        today_btc = df_btc.iloc[i]
        Sell_signal = signal_klay[i]
        Buy_signal = signal_btc[i]
        klay += klay_count
        net.append([today_klay.name, today_klay.Close, 'klay', klay])

        # Sell_klay
        if Sell_signal == -1:
          if klay > 0:
                money += klay * today_klay.Close * commission_fee
                net.append([today_klay.name, today_klay.Close, 'money', money])
                klay = 0

        # Buy_btc
        if Buy_signal == 1:
          if money > 0:
                btc += money / today_btc.Close * commission_fee
                net.append([today_btc.name, today_btc.Close, 'btc', btc])
                money = 0
    return net