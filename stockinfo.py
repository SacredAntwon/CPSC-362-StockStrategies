import yfinance as yf

msft = yf.Ticker("^DJI")

# get stock info

print(msft.info['open'])
