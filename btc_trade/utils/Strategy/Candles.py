import backtrader as bt

class Shootingstar_Strategy(bt.Strategy):

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

        # To keep track of pending orders and buy price/commission
        self.order = None
        self.buyprice = None
        self.buycomm = None

        # Add a CDLSHOOTINGSTAR indicator
        self.CDLSHOOTINGSTAR = bt.talib.CDLSHOOTINGSTAR(self.data.open, self.data.high, self.data.low, self.data.close)

    def next(self):

        # Check if we are in the market
        if not self.position:

            # Not yet ... we MIGHT BUY if ...
            if self.CDLSHOOTINGSTAR[0] > 0:
                # Keep track of the created order to avoid a 2nd order
                self.order = self.buy()

        else:

            if self.CDLSHOOTINGSTAR[0] < 0:

                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()