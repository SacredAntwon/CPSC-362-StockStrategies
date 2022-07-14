import yfinance as yf
import json
import os.path

STOCK_NUMBER = 30

class StockInfo:

    # Initializer

    # -------------------------------------------------------------------

    def __init__(self):

        self.dowJones = {}

    # -------------------------------------------------------------------


    # Methods

    # -------------------------------------------------------------------

    def getJSONData(self, file: str) -> dict:

        # Getting stock tickers from json included in folder
        # f = open('DOW.json')
        f = open(file)
        data = json.load(f)

        return data

    # This function will check if there is a valid key.
    def findInfo(self, currentStock, key):
        if key in currentStock:
            return currentStock[key]
        else:
            return None

    def getAllStockInfo(self) -> list:

        return self.dowJones

    def readJSONFile(self):

        # Check if the file exists
        if not os.path.isfile("userStocks.json"):

            data = self.getJSONData('DOW.json')

            self.storeStockInfo(data)

        else:

            with open('userStocks.json', 'r') as openfile:
 
                # Reading from json file
                self.dowJones = json.load(openfile)

                


    def getStockNames(self) -> list:

        return self.dowJones.keys()

    def storeStockInfo(self, data: dict) -> bool:

        # Return an empty list if the number of stocks is <= 0
        #if stockNumber <= 0 or stockNumber > 30:

        #    return dict()

        # Create the list based off the amount the user inserted.
        listOfStocks = data['DOW'][0:(STOCK_NUMBER)]

        # We have a dictionary for assigning the information to the ticker called dowJones
        # There is also a list called keys for the keys we are looking for.
        # dowJones = {}
        keys = ['open', 'previousClose', 'bid', 'ask', 'volume', 'trailingPE', 'trailingEps']

        for stock in listOfStocks:
            stockInfo = {}
            print(stock)
            currentStock = (yf.Ticker(stock)).info
            for key in keys:
                stockInfo[key] = self.findInfo(currentStock, key)

            self.dowJones[stock] = stockInfo

        with open("userStocks.json", "w") as outfile:
            json.dump(self.dowJones, outfile)

        # Check if the file exists
        if os.path.isfile("userStocks.json"):

            return True

        else:

            return False

    # -------------------------------------------------------------------

