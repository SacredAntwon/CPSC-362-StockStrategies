import Model.data as data
import json
import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA

# STRATEGY PATERN IMPLEMENTED HERE
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

# THIS IS A STRATEGY PATTERN
class SmaCross2(Strategy):
    def init(self):
        self.price = self.data.Close
        self.ma1 = self.I(SMA, self.price, 50)
        self.ma2 = self.I(SMA, self.price, 100)

    def next(self):
        if crossover(self.price, self.ma1):
            self.buy()
        elif crossover(self.price, self.ma2):
            self.sell()

# USED TO DO BACKTESTING AND GET STRATEGY
def grabStrategyData(tickers, cash):
    obj = data.Data()
    if not obj.fileExists("userStrategies.json"):
        money = cash
        stratDict = {}
        for item in tickers:
            stock = data.getHistoricalData(item)
            statsSMA = Backtest(stock, SmaCross, cash=money, commission= 0, exclusive_orders=True)
            statsSMA2 = Backtest(stock, SmaCross2, cash=money, commission= 0, exclusive_orders=True)

            statsSMA = statsSMA.run()
            statsSMA2 = statsSMA2.run()

            stratDict[item] = {}
            stratDict[item]["Trend-Following"] = obj.keepImportantInfo(statsSMA)
            stratDict[item]["PriceSMA"] = obj.keepImportantInfo(statsSMA2)
                

        obj.jsonFileDump("userStrategies.json", stratDict)

    else:
        stratDict = obj.getJSONData("userStrategies.json")

    return stratDict
