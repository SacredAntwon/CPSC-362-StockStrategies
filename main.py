import stockinfo

# Call the functions

# data = stockinfo.getJSONData('DOW.json')

# print(stockinfo.getStockNames(8, data))

obj = stockinfo.StockInfo()

obj.readJSONFile()

#print(obj.getAllStockInfo())
allSocks = obj.getStockNames()

for name in allSocks:
    print(name)

userStock = input("\nType the ticker you would like to view more information \
about(Case Sensitive) or 'exit' to end the program: ")

while (userStock != 'exit'):
    if (userStock not in allSocks):
        print("\nNot A Valid Ticker!")
    else:
        print(obj.displayInfo(userStock))
    userStock = input("Type the ticker you would like to view more information \
about(Case Sensitive) or 'exit' to end the program: ")
