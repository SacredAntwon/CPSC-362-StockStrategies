import stockinfo
import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover, SignalStrategy, TrailingStrategy
from backtesting.test import SMA

#obj = stockinfo.StockInfo()

class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 50)
        self.ma2 = self.I(SMA, price, 100)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()

class SigTrailCross(SignalStrategy,
               TrailingStrategy):
    n1 = 10
    n2 = 20

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

def selectStrategy(strat, ticker):
    obj = stockinfo.StockInfo()
    stock = obj.getStockHistory(ticker)
    money = 1000000

    if strat == 'TF':
        stats = Backtest(stock, SmaCross, cash=money, commission= 0, exclusive_orders=True)

    elif strat == 'ST':
        stats = Backtest(stock, SigTrailCross, cash=money, commission= 0, exclusive_orders=True)

    else:
        return False

    statInfo = stats.run()
    return statInfo
#bt.plot()
#print(stats['Best Trade [%]'])


# class BackTest:
#     def __init__(self):
#         pass
#
#     def movingAverage(self, ticker):
#         stockHistory = obj.getStockHistory(ticker)
#         stockHistory = stockHistory[["Adj Close"]]
#         stockHistory.rename(columns={"Adj Close":"Price"}, inplace=True)
#         stockHistory = stockHistory.iloc[1:]
#         stockHistory["100MA"] = stockHistory["Price"].rolling(window=100).mean()
#         return stockHistory
