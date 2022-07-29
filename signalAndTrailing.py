# import stockinfo
# from scipy import stats
# import statistics
#
# obj = stockinfo.StockInfo()
#
# class MeanReversion:
#
#     def __init__(self):
#         self.linearReg()
#
#     def linearReg(self):
#         y = list(obj.getStockHistory('IBM')["Open"])
#         x = [i for i in range(len(y))]
#
#         slope, intercept, r, p, se = stats.linregress(x, y)
#
#         stdDev = statistics.stdev(y)
#
#         ln1 = [i+stdDev for i in y]
#         ln2 = [i-stdDev for i in y]

        #print("Price: ", y)
        #print("StdDev Above: ", ln1)
        #print("StdDev Below: ", ln2)
        #print(stdDev)
        #print(slope)

import stockinfo
import pandas as pd
from backtesting import Backtest
from backtesting.lib import SignalStrategy, TrailingStrategy
from backtesting.test import SMA

#obj = stockinfo.StockInfo()

class SmaCross(SignalStrategy,
               TrailingStrategy):
    n1 = 50
    n2 = 100

    def init(self):
        # In init() and in next() it is important to call the
        # super method to properly initialize the parent classes
        super().init()

        # Precompute the two moving averages
        sma1 = self.I(SMA, self.data.Close, self.n1)
        sma2 = self.I(SMA, self.data.Close, self.n2)

        # Where sma1 crosses sma2 upwards. Diff gives us [-1,0, *1*]
        signal = (pd.Series(sma1) > sma2).astype(int).diff().fillna(0)
        signal = signal.replace(-1, 0)  # Upwards/long only

        # Use 95% of available liquidity (at the time) on each order.
        # (Leaving a value of 1. would instead buy a single share.)
        entry_size = signal * .95

        # Set order entry sizes using the method provided by
        # `SignalStrategy`. See the docs.
        self.set_signal(entry_size=entry_size)

        # Set trailing stop-loss to 2x ATR using
        # the method provided by `TrailingStrategy`
        self.set_trailing_sl(2)

#stock = obj.getStockHistory('IBM')

#bt = Backtest(stock, SmaCross, cash=100000, commission= 0,
              #exclusive_orders=True)
#stats = bt.run()
#bt.plot()
#print(stats['Best Trade [%]'])
