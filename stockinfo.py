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

    # Checks if a file exists
    def fileExists(self, file: str) -> bool:

        # Check if the file exists
        if os.path.isfile(file):

            return True

        else:

            return False

    # Gets information from json
    def getJSONData(self, file: str) -> dict:
        # Getting stock tickers from json included in folder
        f = open(file)
        data = json.load(f)

        return data

    # This function will convert the information to a string.
    def displayInfo(self, currentStock):
        currentStockInfo = self.getStockInfo(currentStock)
        return ("\nTicker: {} \nOpen: {}\nClose: {}\nBid: {} \nAsk: {}\nVolume: \
{}\nPE Ratio: {}\nEPS: {}\nRecommendation: Firm - {}  Grade - {}\n".format(currentStock,
currentStockInfo['open'], currentStockInfo['previousClose'], currentStockInfo['bid'],
currentStockInfo['ask'], currentStockInfo['volume'], currentStockInfo['trailingPE'],
currentStockInfo['trailingEps'], currentStockInfo['recommend']['firm'],
currentStockInfo['recommend']['grade']))

    # This function will check if there is a valid key.
    def findInfo(self, currentStock, key):
        if key in currentStock:
            return currentStock[key]
        else:
            return None

    # Return the info from a dictionary about a stock
    def getStockInfo(self, currentStock):

        return self.dowJones[currentStock]

    # Gets all the stock tickers and their information
    def getAllStockInfo(self) -> list:

        return self.dowJones

    # Gets all the stock tickers from the dictionary
    def getStockNames(self) -> list:

        return self.dowJones.keys()

    # Either call the function to grab the stock information from yfinance or
    # if our json exists, read the userStocks.json and grab the information.
    def readJSONFile(self):

        # Check if the file exists
        if not self.fileExists("userStocks.json"):
            print("Getting stock information from yahoo!")

            data = self.getJSONData('DOW.json')

            self.storeStockInfo(data)

        else:

            with open('userStocks.json', 'r') as openfile:

                # Reading from json file
                self.dowJones = json.load(openfile)

    # Grab and store stock infromation
    def storeStockInfo(self, data: dict) -> bool:

        listOfStocks = data['DOW']

        # We have a dictionary for assigning the information to the ticker called dowJones
        # There is also a list called keys for the keys we are looking for.

        keys = ['open', 'previousClose', 'bid', 'ask', 'volume', 'trailingPE', 'trailingEps']

        # Loop through all the tickers and grab the information from yfinance
        for stock in listOfStocks:
            stockInfo = {}
            print(stock)
            currentStock = (yf.Ticker(stock)).info
            recommendStock = (yf.Ticker(stock)).recommendations
            recoList = {"firm": recommendStock["Firm"][-1], "grade": recommendStock["To Grade"][-1]}
            for key in keys:
                stockInfo[key] = self.findInfo(currentStock, key)

            stockInfo["recommend"] = recoList

            self.dowJones[stock] = stockInfo

        with open("userStocks.json", "w") as outfile:
            json.dump(self.dowJones, outfile)

        return self.fileExists("userStocks.json")

    # -------------------------------------------------------------------
