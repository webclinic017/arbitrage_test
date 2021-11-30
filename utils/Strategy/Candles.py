def Shootingstar_Strategy(klay_count,commission_fee,df_klay,df_btc) :
    def signal(df) :
        df = df.ta.cdl_pattern(name="shootingstar")
        return list(df['CDL_SHOOTINGSTAR'])

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