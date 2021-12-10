from utils.Risk_Function import CPPI_Strategy


def Portfolio(total_klay,klay_count,commision_fee,df_klay,df_btc,signal_klay,signal_btc) :

    total_money = total_klay * df_klay.Close.iloc[0]
    btc = 0
    net = []
    tmp_balance1,tmp_balance2 = total_money,0

    for i in range(len(df_btc)):
      if i <= 2 :
        cppi,cushion,klay, money = CPPI_Strategy(klay_count,tmp_balance1,tmp_balance2,i,cppi = 1)
      else : 
        cppi,cushion,klay, money = CPPI_Strategy(klay_count,tmp_balance1,tmp_balance2,i,cppi,cushion)

      today_klay = df_klay.iloc[i]
      today_btc = df_btc.iloc[i]
      Sell_signal = signal_klay[i]
      Buy_signal = signal_btc[i]

      # Sell_klay
      if Sell_signal == -1:
        if (total_klay - klay) > 0:
              total_money += klay * today_klay.Close * commision_fee
              total_klay -= klay

      # Buy_btc
      if Buy_signal == 1:
        if (total_money - money) > 0:
              btc += money / today_btc.Close * commision_fee
              total_money -= money

      total_balance = (total_klay * today_klay.Close) + (total_money) + (btc * today_btc.Close)
      tmp_balance2 = tmp_balance1
      tmp_balance1 = total_balance

      net.append([today_klay.name, today_klay.Close, 'klay', total_klay])
      net.append([today_klay.name, today_klay.Close, 'money', total_money])
      net.append([today_btc.name, today_btc.Close, 'btc', btc])
      net.append([today_klay.name, today_klay.Close, 'balance', total_balance])

    return net