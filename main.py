import Model.data as data
import backtest
import Model.strategy as strategy
import view
from backtesting import Backtest, Strategy

# Call the functions

if __name__ == '__main__':

    print("Getting stock information...")
    sinfo = data.Data()

    print("Running all strategies...")

    strat = strategy.grabStrategyData(sinfo.getStockNames(), 1000000)

    print("Running the display!")

    # Run the display
    gui = view.View(sinfo, strat)
    gui.mainloop()