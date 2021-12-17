def CPPI_Strategy(klay_count,tmp_balance1 ,tmp_balance2 ,i ,cppi, *cushion) :
    m = 5
    floor_value = 0.92
    if i <= 2 : ## 첫날

      cushion = cppi - floor_value
      klay = klay_count
      money = tmp_balance1
        
    else :
      ret = tmp_balance1 - tmp_balance2 / tmp_balance2
      if abs(ret) > 1 : ret = 0
      E = max(min(int(cushion[0]) * m, cppi), 0) # 내 재산 갖고 콜옵션 m개를 사자.
      B = cppi - E # 콜옵션 m개 사고 남는 돈은 현금으로 갖고 있자.
      E_next = E * (1+ret)
      cppi = E_next + B * (1+0.015)
      
      cushion = cppi - floor_value # 콜옵션 가격을 트래킹하는 것임.

      klay = klay_count * E
      money = tmp_balance1 / 5 * E

    return cppi,cushion,klay, money