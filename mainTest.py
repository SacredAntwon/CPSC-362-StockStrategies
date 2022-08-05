import stockinfo
import backtest
import strategy
from backtesting import Backtest, Strategy

# Call the functions
obj = stockinfo.StockInfo()
#backt = backtest.SMAcross()

obj.portfolioInfo("Add", "CLAY")
#obj.portfolioInfo("Add", info, "SET")

#bt = Backtest(obj.getStockHistory('IBM'), backt, cash=100000, commission = 0.002, exclusive_orders=True)
print("Getting stock information from Yahoo Finance. Please wait a few seconds!")

obj.readJSONFile()

allStocks = obj.getStockNames()
allStockStrategies = strategy.grabStrategyInfo(allStocks, 1000000)
#print(allStockStrategies)
# Display all stocks to choose from
for name in allStocks:
    print(name)

# Get the list of prices (this information will be passed to the backtesting class)
#prices = obj.getStockHistory("AAPL")["Open"]

#prices = obj.getStockHistory("HD")["Open"]

#print(prices)

#bt = backtesting.Backtesting(100000, prices, 0)




# Uncomment this chunk of lines later if testing is needed
print("Select a stock from the list above.")
userStock = input("\nType the ticker you would like to view more information \
about(Case Sensitive) or 'exit' to end the program: ")
userStrategy = input("\nType the strategy you would like to view (TF or ST): ")

while (userStock != 'exit'):
    if (userStock not in allStocks):
        print("\nNot A Valid Ticker!")
    else:
        print(obj.displayInfo(userStock))
        print(allStockStrategies[userStock][userStrategy])

    userStock = input("Type the ticker you would like to view more information \
about(Case Sensitive) or 'exit' to end the program: ")
    userStrategy = input("\nType the strategy you would like to view (TF or ST): ")
