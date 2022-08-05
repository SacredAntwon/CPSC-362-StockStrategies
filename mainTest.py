import stockinfo
import backtest
import strategy
from backtesting import Backtest, Strategy

# Call the functions
obj = stockinfo.StockInfo()


obj.portfolioInfo("Remove", "CLAY", "PriceSMA")

print("Getting stock information from Yahoo Finance. Please wait a few seconds!")

obj.readJSONFile()

allStocks = obj.getStockNames()
allStockStrategies = strategy.grabStrategyInfo(allStocks, 1000000)

# Display all stocks to choose from
for name in allStocks:
    print(name)

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
