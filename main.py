import stockinfo
#import backtest
# Call the functions

obj = stockinfo.StockInfo()
#backt = backtest.BackTest()

print("Getting stock information from Yahoo Finance. Please wait a few seconds!")

obj.readJSONFile()

allStocks = obj.getStockNames()

# Display all stocks to choose from
for name in allStocks:
    print(name)

# Get the list of prices (this information will be passed to the backtesting class)
prices = obj.getStockHistory("AAPL")["Adj Close"]

print(len(prices))

print("Select a stock from the list above.")
userStock = input("\nType the ticker you would like to view more information \
about(Case Sensitive) or 'exit' to end the program: ")

while (userStock != 'exit'):
    if (userStock not in allStocks):
        print("\nNot A Valid Ticker!")
    else:
        print(obj.displayInfo(userStock))
        #print(backt.movingAverage(userStock))
        #print(obj.getStockHistory(userStock))
        #stock = obj.getStockHistory(userStock)
        #print(stock)
        #backtest.getStats(stock)
        #print(backtest.getStats(stock))
    userStock = input("Type the ticker you would like to view more information \
about(Case Sensitive) or 'exit' to end the program: ")
