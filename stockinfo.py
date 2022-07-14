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

def getStockNames(stockNumber: int, data: dict) -> dict:

    # Return an empty list if the number of stocks is <= 0
    if stockNumber <= 0 or stockNumber > 30:

        return dict()

    # Create the list based off the amount the user inserted.
    listOfStocks = data['DOW'][0:(stockNumber)]

    # We have a dictionary for assigning the information to the ticker called dowJones
    # There is also a list called keys for the keys we are looking for.
    dowJones = {}
    keys = ['open', 'previousClose', 'bid', 'ask', 'volume', 'trailingPE', 'trailingEps']

    for stock in listOfStocks:
        stockInfo = {}
        print(stock)
        currentStock = (yf.Ticker(stock)).info
        for key in keys:
            stockInfo[key] = findInfo(currentStock, key)

        dowJones[stock] = stockInfo

    return dowJones

# Call the functions

data = getJSONData('DOW.json')

print(getStockNames(8, data))