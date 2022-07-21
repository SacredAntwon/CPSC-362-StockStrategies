import tkinter as tk
from tkinter import ttk
import stockinfo

class DisplayClass(tk.Tk):

    # This initializer places all widgets within their corresponding frame
    def __init__(self):
        super().__init__()

        #self.geometry("240x100")
        self.geometry("900x1200")
        self.title('Login')
        #self.resizable(0, 0)

        # configure the columns in the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=5)
        self.rowconfigure(2, weight=4)

        self.create_stockinfo()
        self.create_buttons()

    # This function creates the widgets for all stock info
    def create_stockinfo(self):

        # Note: A scrollbar requires a Canvas, which needs to encompass the Frame and it's a mess we don't want to deal with

        # These two variables will be declared as global in stockinfo.py

        obj = stockinfo.StockInfo()

        obj.readJSONFile()

        stockDict = obj.dowJones
        stockData = obj.keys
        stockNames = obj.getStockNames()

        # Create the underlying frame that holds all stock information
        stockInfo = tk.Frame(self)
        stockInfo.grid(column=1, row=1)

        categories = ["Stock", "Open", "Close", "Bid", "Ask", "Vol", "PE", "EPS", "ARat"]

        for index in range(len(categories)):

            # Create each category inside the stockInfo frame
            stockCategory = tk.Label(stockInfo, text=categories[index])
            stockCategory.grid(column=index, row=0)

        # Add here the displays for each stock retrieved from the API call
        for i in range(len(stockNames)):

            stockName = tk.Label(stockInfo, text=stockNames[i], highlightcolor="blue", highlightthickness=4)
            stockName.grid(column=0, row=i+1)

            for j in range(len(stockData)):

                stockCategory = tk.Label(stockInfo, text=stockDict[stockNames[i]][stockData[j]])
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


    def create_buttons(self):

        #stockButtons = tk.Frame(self)
        #stockButtons.grid(column=1, row=0)

        """# Create the Display Stocks button
        displayStocks = tk.Button(self, text="Display Stocks")
        displayStocks.grid(column=0, row=1)

        # Create the menu for backtesting
        menu = tk.StringVar()
        menu.set("Backtesting Options")

        # Create the information to be displayed in the dropdown
        dropDown = tk.OptionMenu(self, menu, "Option1", "Option2")
        dropDown.grid(column=1, row=1)

        # Create the Show Profile button
        displayStocks = tk.Button(self, text="Show Profile")
        displayStocks.grid(column=2, row=1)"""

        #stockButtons = tk.Frame(self)
        #stockButtons.grid(column=1, row=0)

        # Create the Display Stocks button
        displayStocks = tk.Button(self, text="Display Stocks", bg="lightblue")
        displayStocks.grid(column=1, row=0, sticky=tk.SW)

        # Create the menu for backtesting
        menu = tk.StringVar()
        menu.set("Backtesting Options")

        # Create the information to be displayed in the dropdown
        dropDown = tk.OptionMenu(self, menu, "Option1", "Option2")
        dropDown.config(bg="lightgray")
        dropDown.grid(column=1, row=0, sticky=tk.S)

        # Create the Show Profile button
        displayStocks = tk.Button(self, text="Show Profile", bg="lightgreen")
        displayStocks.grid(column=1, row=0, sticky=tk.SE)

    #def add_portfolio(self):



if __name__ == "__main__":

    # Create an instance of our app
    app = DisplayClass()

    # This function displays the app to the screen
    app.mainloop()
