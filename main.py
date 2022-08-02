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

    print("Getting stock information...")
    sinfo = stockinfo.StockInfo()
    sinfo.readJSONFile()

    print("Running all strategies...")

    strat = strategy.grabStrategyInfo(sinfo.getStockNames(), 1000000)

    print("Running the display!")

    # Run the display
    gui = display.DisplayClass(sinfo, strat)
    gui.mainloop()
