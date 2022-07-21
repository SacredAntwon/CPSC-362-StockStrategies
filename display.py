import tkinter as tk
from tkinter import ttk
import stockinfo

class DisplayClass(tk.Tk):

    # This initializer places all widgets within their corresponding frame
    def __init__(self):
        super().__init__()

        #self.geometry("240x100")
        self.geometry("900x600")
        self.title('Login')
        # self.resizable(0, 0)

        # configure the columns in the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=6)
        self.rowconfigure(1, weight=6)
        self.rowconfigure(2, weight=5)

        self.create_stockinfo()

    # This function creates the widgets for all stock info
    def create_stockinfo(self):

        # These two variables will be declared as global in stockinfo.py

        obj = stockinfo.StockInfo()

        obj.readJSONFile()

        stockDict = obj.dowJones
        stockNames = ['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS', 'DOW', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH', 'V', 'VZ', 'WBA', 'WMT']
        stockData = ["regularMarketOpen", "regularMarketPreviousClose", "bid", "ask", "regularMarketVolume", "trailingPE", "epsTrailingTwelveMonths", "averageAnalystRating"]

        # Create the underlying frame that holds all stock information
        stockInfo = tk.Frame(self)
        stockInfo.grid(column=1, row=1)

        categories = ["Stock", "Open", "Close", "Bid", "Ask", "Vol", "PE", "EPS", "ARat"]

        for index in range(len(categories)):

            # Create each category inside the stockInfo frame
            stockCategory = tk.Label(stockInfo, text=categories[index], font='Verdana 13 underline')
            stockCategory.grid(column=index, row=0)

        # Add here the displays for each stock retrieved from the API call
        for i in range(len(stockNames)):

            stockName = tk.Label(stockInfo, text=stockNames[i], font='Verdana 13 underline')
            stockName.grid(column=0, row=i+1)

            for j in range(len(stockData)):

                stockCategory = tk.Label(stockInfo, text=stockDict[stockNames[i]][stockData[j]], font='Verdana 13 underline')
                stockCategory.grid(column=j+1, row=i+1)

        #myButton.pack()
        #stockInfo.pack()

        """# username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        username_entry = ttk.Entry(self)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self,  show="*")
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(self, text="Login")
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)"""


if __name__ == "__main__":

    # Create an instance of our app
    app = DisplayClass()

    # This function displays the app to the screen
    app.mainloop()
