import json
import os.path
import requests
import time
import datetime
import pandas as pd
from requests.exceptions import Timeout
import yfinance as yf

# FINISHED API DEMO AND PASSED AT July 19th 8:01 PM
# ADAPTER PATTERN IMPLEMENTED HERE
class HistoricalDataAdapter():
    def __init__(self, **adapted_method):
        self.__dict__.update(adapted_method)

def getHistoricalData(ticker, data_source="API"):
    if data_source == "API":
        hd = StockInfoAPI(ticker)

    elif data_source == "Yahoo":
        hd = StockInfoYF(ticker)

    data_adapter = HistoricalDataAdapter(historical_data = hd.getStockHistory)
    hdata = data_adapter.historical_data()

    return hdata

# ADAPTEE PATTERN IMPLEMENTED HERE
class StockInfoAPI():
    def __init__(self, ticker):
        self.ticker = ticker

    def getStockHistory(self):
        #Year, Month, Day, Hour, Minute
        period1 = int(time.mktime(datetime.datetime(1980, 1, 1, 23, 59).timetuple()))
        period2 = int(time.mktime(datetime.datetime(2025, 12, 30, 23, 59).timetuple()))
        interval = '1d' # 1d, 1m, 1wk

        query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{self.ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

        df = pd.read_csv(query_string, index_col='Date', parse_dates=True)
        return df

# ADAPTEE PATTERN IMPLEMENTED HERE
class StockInfoYF():
    def __init__(self, ticker):
        self.ticker = ticker

    def getStockHistory(self):
        hist = yf.Ticker(self.ticker).history(period="max")

        return hist

# CONTAINS MANY FUNCTIONS TO GRAB INFORMATION ABOUT A STOCK
class StockInfo:

    # Initializer

    # -------------------------------------------------------------------

    def __init__(self):

        self.dowJones = {}
        self.keys = ['regularMarketOpen', 'regularMarketPreviousClose', 'bid', 'ask', 'regularMarketVolume', 'trailingPE', 'epsTrailingTwelveMonths', 'averageAnalystRating']
    # -------------------------------------------------------------------


    # Methods

    # -------------------------------------------------------------------



    def keepImportantInfo(self, stats):
        statDict = {'annualReturn': stats['Return (Ann.) [%]'],
                    'profitFactor': stats['Profit Factor'],
                    'winRate': stats['Win Rate [%]'],
                    'maxDrawdown': stats['Max. Drawdown [%]'],
                    'annualVolatility': stats['Volatility (Ann.) [%]'],
                    'sharpeRatio': stats['Sharpe Ratio']}

        return statDict

    # Check if the file exists
    def fileExists(self, file: str) -> bool:
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
    # DECORATOR PATTERN IMPLEMETED HERE
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

    def getKeys(self) -> list:

        return self.keys

    # Gets all the stock tickers from the dictionary
    def getStockNames(self) -> list:

        return list(self.dowJones.keys())

    # Either call the function to grab the stock information from yfinance or
    # if our json exists, read the userStocks.json and grab the information.
    def readJSONFile(self):

        data = self.getJSONData('DOW.json')

        if not self.fileExists("userStocks.json"):
            if self.fileExists("userStrategies.json"):
                os.remove("userStrategies.json")
            self.storeStockInfo(data)

        else:
            self.dowJones = self.getJSONData("userStocks.json")

    # Store info into portfolio json
    def portfolioInfo(self, todo, ticker, strat):

        # Check if the portfolio file exists
        if not self.fileExists("portfolio.json"):

            if not self.createEmptyJSONFile("portfolio.json"):

                print("Error! Unable to create portfolio.json!")
                return False

            else:

                # Data only contains the portfolio
                data = {'portfolio': []}

        else:

            data = self.getJSONData('portfolio.json')

        item = [ticker, strat]

        if (todo == "Add"):
            if item not in data['portfolio']:
                data['portfolio'].append(item)

        elif (todo == "Remove"):
            if item in data['portfolio']:
                data['portfolio'].remove(item)

        self.jsonFileDump("portfolio.json", data)

        print(data)

    def createEmptyJSONFile(self, fileName):

        try:
            
            open(fileName, "x")

            return True

        except:

            return False

    # Grab and store stock infromation
    def jsonFileDump(self, fileName, data):
        with open(fileName, "w") as outfile:
            json.dump(data, outfile)

    # Store the stock info
    def storeStockInfo(self, data: dict) -> bool:

        listOfStocks = data['DOW']
        url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols="

        # Loop through all the tickers and grab the information from yfinance
        for stock in listOfStocks:
            stockInfo = {}
            stockLink = url+stock
            headers={'User-agent': 'Mozilla/5.0'}

            try:
                response = requests.get(stockLink, headers=headers, timeout=10)
                response.close()
            except Exception as err:
                print("Got an error! " + str(err))
                if self.fileExists("userStocks.json"):
                    self.dowJones = self.getJSONData("userStocks.json")
                    return True
                else:
                    return False

            if (response.status_code != 200):
                if self.fileExists("userStocks.json"):
                    self.dowJones = self.getJSONData("userStocks.json")
                    return True
                else:
                    return False
            else:
                currentStock = response.json()["quoteResponse"]["result"][0]

            for key in self.keys:
                stockInfo[key] = self.findInfo(currentStock, key)

            self.dowJones[stock] = stockInfo

        self.jsonFileDump("userStocks.json", self.getAllStockInfo())

        return True

    # This function separates the strategy from the ticker
    def separateStrategies(self, ticker_strategy):

        # TODO: Find a way to make this function return an array of all strategies AND the number
        #       of tickers belonging to each strategy (probably using a multi-dimensional array)

        # This is the list that stores each strategy in ticker_strategy
        strategyList = []

        # The list of tickers for each corresponding strategy
        tickerList = []

        # Whether or not the strategy was found in the strategyList
        strategyWasFound = False

        # Iterate through every ticker sub-array in ticker_strategy
        for i in range(len(ticker_strategy)):

            for j in range(len(strategyList)):

                if ticker_strategy[i][1] == strategyList[j]:

                    # We found the strategy
                    strategyWasFound = True

                    # At index j, append the new ticker
                    tickerList[j].append(ticker_strategy[i][0])
            
            # Check if the strategy wasn't found
            if not strategyWasFound:

                # Append the new strategy to the strategyList
                strategyList.append(ticker_strategy[i][1])

                # Append the first ticker (inside a list) to the tickerList
                tickerList.append([ticker_strategy[i][0]])

            # Reset the strategyWasFound flag
            strategyWasFound = False

            """# Check if the strategy associated with the stock isn't registered in strategyList
            if ticker_strategy[i][1] not in strategyList:

                # Append the strategy to the strategy list
                strategyList.append(ticker_strategy[i][1])

                # Append the ticker to the ticker list
                tickerList.append([ticker_strategy[i][0]])

            # This means the strategy already exists in our strategy list, so we need to find it
            else:"""

            
        # Return the tickerList (a multi-dimensional array) and strategyList (an array)
        return tickerList, strategyList

    # -------------------------------------------------------------------
