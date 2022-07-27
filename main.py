import stockinfo
import backtest
# Call the functions

obj = stockinfo.StockInfo()
backt = backtest.BackTest()

print("Getting stock information from Yahoo Finance. Please wait a few seconds!")

obj.readJSONFile()

allSocks = obj.getStockNames()



# Display all stocks to choose from
for name in allSocks:
    print(name)

print("Select a stock from the list above.")
userStock = input("\nType the ticker you would like to view more information \
about(Case Sensitive) or 'exit' to end the program: ")

while (userStock != 'exit'):
    if (userStock not in allSocks):
        print("\nNot A Valid Ticker!")
    else:
        print(obj.displayInfo(userStock))
        print(backt.movingAverage(userStock))
        #print(obj.getStockHistory(userStock))
        #stock = obj.getStockHistory(userStock)
        #print(stock)
        #backtest.getStats(stock)
        #print(backtest.getStats(stock))
    userStock = input("Type the ticker you would like to view more information \
about(Case Sensitive) or 'exit' to end the program: ")
