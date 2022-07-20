import json
import os.path
import requests

# FINISHED API DEMO AND PASSED AT July 19th 8:01 PM
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
{}\nPE Ratio: {}\nEPS: {}\nRecommendation: {}\n".format(currentStock,
currentStockInfo['regularMarketOpen'], currentStockInfo['regularMarketPreviousClose'], currentStockInfo['bid'],
currentStockInfo['ask'], currentStockInfo['regularMarketVolume'], currentStockInfo['trailingPE'],
currentStockInfo['epsTrailingTwelveMonths'], currentStockInfo['averageAnalystRating']))

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

        print("Getting stock information from Yahoo Finance. Please wait a few seconds!")
        data = self.getJSONData('DOW.json')

        self.storeStockInfo(data)
        # Check if the file exists
        # if not self.fileExists("userStocks.json"):
        #     print("Getting stock information from yahoo!")
        #
        #     data = self.getJSONData('DOW.json')
        #
        #     self.storeStockInfo(data)
        #
        # else:
        #
        #     with open('userStocks.json', 'r') as openfile:
        #
        #         # Reading from json file
        #         self.dowJones = json.load(openfile)

    # Grab and store stock infromation
    def storeStockInfo(self, data: dict) -> bool:

        listOfStocks = data['DOW']
        url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols="


        # We have a dictionary for assigning the information to the ticker called dowJones
        # There is also a list called keys for the keys we are looking for.

        keys = ['regularMarketOpen', 'regularMarketPreviousClose', 'bid', 'ask', 'regularMarketVolume', 'trailingPE', 'epsTrailingTwelveMonths', 'averageAnalystRating']

        # Loop through all the tickers and grab the information from yfinance
        for stock in listOfStocks:
            stockInfo = {}
            stockLink = url+stock

            response = requests.get(stockLink, headers={'User-agent': 'Mozilla/5.0'})
            currentStock = response.json()["quoteResponse"]["result"][0]

            for key in keys:
                stockInfo[key] = self.findInfo(currentStock, key)

            self.dowJones[stock] = stockInfo

        with open("userStocks.json", "w") as outfile:
            json.dump(self.dowJones, outfile)

        return self.fileExists("userStocks.json")

    # -------------------------------------------------------------------
