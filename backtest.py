import stockinfo

obj = stockinfo.StockInfo()

class BackTest:
    def __init__(self):
        pass

    def movingAverage(self, ticker):
        stockHistory = obj.getStockHistory(ticker)s
        stockHistory = stockHistory[["Adj Close"]]
        stockHistory.rename(columns={"Adj Close":"Price"}, inplace=True)
        stockHistory = stockHistory.iloc[1:]
        stockHistory["100MA"] = stockHistory["Price"].rolling(window=100).mean()
        return stockHistory
