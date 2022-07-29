import stockinfo
from scipy import stats
import statistics

obj = stockinfo.StockInfo()

class MeanReversion:

    def __init__(self):
        self.linearReg()

    def linearReg(self):
        y = list(obj.getStockHistory('IBM')["Open"])
        x = [i for i in range(len(y))]

        slope, intercept, r, p, se = stats.linregress(x, y)

        stdDev = statistics.stdev(y)

        ln1 = [i+stdDev for i in y]
        ln2 = [i-stdDev for i in y]
        #print("Price: ", y)
        #print("StdDev Above: ", ln1)
        #print("StdDev Below: ", ln2)
        #print(stdDev)
        #print(slope)
