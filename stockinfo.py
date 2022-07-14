import yfinance as yf
import json

def getJSONData(file: str) -> dict:

    # Getting stock tickers from json included in folder
    # f = open('DOW.json')
    f = open(file)
    data = json.load(f)

    return data

# This function will check if there is a valid key.
def findInfo(currentStock, key):
    if key in currentStock:
        return currentStock[key]
    else:
        return None

def getStockNames(stockNumber: int, data: dict) -> list:

    # This is the array of stock names that will be returned from this function
    stockNameList = []
    stockInfoList = []

    # Return an empty list if the number of stocks is <= 0
    if stockNumber <= 0 or stockNumber > 30:

        return []

    # Create the list based off the amount the user inserted.
    listOfStocks = data['DOW'][0:(stockNumber)]

    # We have a dictionary for assigning the information to the ticker called dowJones
    # There is also a list called keys for the keys we are looking for.
    # dowJones = {}
    keys = ['open', 'previousClose', 'bid', 'ask', 'volume', 'trailingPE', 'trailingEps']

    for stock in listOfStocks:
        # stockInfo = []
        print(stock)
        stockNameList.append(stock)
        currentStock = (yf.Ticker(stock)).info
        values = []
        for key in keys:
            values.append(findInfo(currentStock, key))

        stockInfoList.append(values)

        # dowJones[stock] = stockInfoList

    return [stockNameList, stockInfoList]

# Call the functions

data = getJSONData('DOW.json')

print(getStockNames(8, data))


"""def getStockInfo(stockNumber: int)

    # Ask the user the number of stocks they would like to look at
    stockNumber = int(input("Enter the number of stocks in Dow Jones you would \
    like to check (Insert a number between 1 and 30 inclusive): "))

    # If a number under or over the suggested amount will enter a loop until
    # the valid amount is insterted.
    while (stockNumber < 1 or stockNumber > 30):
        stockNumber = int(input("Invalid Amount! Enter the number of stocks in \
    Dow Jones you would like to check (Insert a number between 1 and 30 \
    inclusive): "))

    # Create the list based off the amount the user inserted.
    listOfStocks = data['DOW'][0:(stockNumber)]

    print("\nGetting stock information. This may take a couple minutes depending \
    on the number of stocks selected.")

    # We have a dictionary for assigning the information to the ticker called dowJones
    # There is also a list called keys for the keys we are looking for.
    dowJones = {}
    keys = ['open', 'previousClose', 'bid', 'ask', 'volume', 'trailingPE', 'forwardEps']

    # This loop will get all the stock tickers and assign all the information to the
    # tickers in the dictionary.
    for stock in listOfStocks:
        stockInfo = []
        print(stock)
        currentStock = (yf.Ticker(stock)).info
        for key in keys:
            stockInfo.append(findInfo(currentStock, key))

        dowJones[stock] = stockInfo

    selectedStock = input("Enter the stock ticker from the list you would like \
    to look at or type 'exit' to end the program: ")

    while (selectedStock != "exit"):
        if selectedStock in listOfStocks:
            print("{}: {}".format(selectedStock, dowJones[selectedStock]))
        else:
            print("Invalid ticker!")

        selectedStock = input("Enter the stock ticker from the list you would like \
    to look at or type 'exit' to end the program: ")"""


