import stockinfo

# Call the functions

# data = stockinfo.getJSONData('DOW.json')

# print(stockinfo.getStockNames(8, data))

obj = stockinfo.StockInfo()

obj.readJSONFile()

print(obj.getAllStockInfo())