import stockinfo
import backtest
import strategy
from backtesting import Backtest, Strategy

# Call the functions
#meanr = meanrev.MeanReversion()

obj = stockinfo.StockInfo()
#backt = backtest.SMAcross()

#bt = Backtest(obj.getStockHistory('IBM'), backt, cash=100000, commission = 0.002, exclusive_orders=True)
print("Getting stock information from Yahoo Finance. Please wait a few seconds!")

obj.readJSONFile()

allStocks = obj.getStockNames()

# Display all stocks to choose from
for name in allStocks:
    print(name)

# Get the list of prices (this information will be passed to the backtesting class)
#prices = obj.getStockHistory("AAPL")["Open"]

#prices = obj.getStockHistory("HD")["Open"]

#print(prices)

#bt = backtesting.Backtesting(100000, prices, 0)


# Uncomment this after you're done testing

#print(len(prices))
def runBackTest(ticker):
    stock = obj.getStockHistory(ticker)

    movingAvg = Backtest(stock, strategy.SmaCross, cash=100000, commission= 0, exclusive_orders=True)

    sigAndTrail = Backtest(stock, strategy.SigTrailCross, cash=100000, commission= 0, exclusive_orders=True)

    statsMove = movingAvg.run()
    statsSigTrail = sigAndTrail.run()

    print(obj.keepImportantInfo(statsMove))
    print(obj.keepImportantInfo(statsSigTrail))

print("Select a stock from the list above.")
# Uncomment this chunk of lines later if testing is needed
print("Select a stock from the list above.")
userStock = input("\nType the ticker you would like to view more information \
about(Case Sensitive) or 'exit' to end the program: ")

while (userStock != 'exit'):
    if (userStock not in allStocks):
        print("\nNot A Valid Ticker!")
    else:
        print(obj.displayInfo(userStock))
        runBackTest(userStock)
        #print(backt.movingAverage(userStock))
        #print(obj.getStockHistory(userStock))
        #stock = obj.getStockHistory(userStock)
        #print(stock)
        #backtest.getStats(stock)
        #print(backtest.getStats(stock))
    userStock = input("Type the ticker you would like to view more information \
about(Case Sensitive) or 'exit' to end the program: ")
