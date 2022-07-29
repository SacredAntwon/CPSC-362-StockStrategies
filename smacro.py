import stockinfo
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
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
