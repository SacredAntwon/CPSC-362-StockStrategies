import stockinfo
import backtest
import strategy
import display
from backtesting import Backtest, Strategy
#import smacro
#import meanrev
# Call the functions
#meanr = meanrev.MeanReversion()

if __name__ == '__main__':
    obj = stockinfo.StockInfo()
    obj.readJSONFile()
    strategy.grabStrategyInfo(obj.getStockNames(), 1000000)
    display.DisplayClass()
