import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import stockinfo

class DisplayClass(tk.Tk):

    # This initializer places all widgets within their corresponding frame
    def __init__(self):
        super().__init__()

        #self.geometry("240x100")
        self.geometry("900x1200")
        self.title('Main Page')
        #self.resizable(0, 0)

        # configure the columns in the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # Initialize the stockinfo object by getting stock info
        # TODO: Remove the makeAPICalls() function and pass the info to __init__() from main.py
        self.makeAPICalls()

        self.create_layout()

    # This function calls all functions related to displaying GUI information
    def create_layout(self):

        # Place the information from the API call in the GUI
        self.create_display_stock_info()

        self.create_search()

        self.create_portfolio()

    def makeAPICalls(self):

        # Create the object
        self.obj = stockinfo.StockInfo()

        # Read from the JSON file
        self.obj.readJSONFile()

        # Store all relevant information in local variables within our class
        self.stockDict = self.obj.dowJones
        self.stockData = self.obj.keys
        self.stockNames = self.obj.getStockNames()

    # This function creates the widgets for all stock info
    def create_display_stock_info(self):

        # Note: A scrollbar requires a Canvas, which needs to encompass the Frame and it's a mess we don't want to deal with

        # These two variables will be declared as global in stockinfo.py

        obj = stockinfo.StockInfo()

        obj.readJSONFile()

        stockDict = obj.dowJones
        stockData = obj.keys
        stockNames = obj.getStockNames()

        # Create the underlying frame that holds all stock information
        stockInfo = tk.Frame(self)
        stockInfo.grid(column=1, row=1, sticky=tk.N)

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

    # This function is used to create the search mechanics, including the ticker dropdown, strategy dropdown and search button
    def create_search(self):

        # Create the frame the contains this information and place it on the grid above the stock information
        searchFrame = tk.Frame(self)
        searchFrame.grid(column=1, row=0)

        # Within the frame, display a "Ticker" Label
        tickerLabel = tk.Label(searchFrame, text="Ticker: ", font="BOLD")
        tickerLabel.grid(column=0, row=0)

        # Within the frame, display a "Strategy" Label
        strategyLabel = tk.Label(searchFrame, text="Strategy: ", font="BOLD")
        strategyLabel.grid(column=0, row=1)

        # Within the frame, display a "Search" Button
        # TODO: Modify this search button to call a function to create a new window
        searchButton = tk.Button(searchFrame, text="Search")
        searchButton.config(bg="lightgray")
        searchButton.grid(column=1, row=2, pady=10)

        # Create a list containing the ticker name information in the dropdown menu
        tickerNames = self.stockNames

        # Create a list containing the list of all strategy names
        # Note: This is hard coded, but can be changed later if needed
        strategyNames = ["Trend-Following", "Signal-And-Trailing"]

        # Create the variable to store user input from the dropdown regarding ticker names
        # TODO: Somehow pass this variable to the smacro.py or signalAndTrailing.py files to
        #       get the result when running a strategy
        tickerInput = tk.StringVar()

        # Create the variable to store user input from the dropdown regarding strategies
        # TODO: Somehow pass this variable to the smacro.py or signalAndTrailing.py files to
        #       get the result when running a strategy
        strategyInput = tk.StringVar()

        # Display the dropdown menu containing all ticker names, change the color and place it on the grid
        tickerDropdown = tk.OptionMenu(searchFrame, tickerInput, *tickerNames)
        tickerDropdown.config(bg="lightblue", width=20)
        tickerDropdown.grid(column=1, row=0)

        # Display the dropdown menu containing all strategy names, change the color and place it on the grid
        strategyDropdown = tk.OptionMenu(searchFrame, strategyInput, *strategyNames)
        strategyDropdown.config(bg="gold", width=20)
        strategyDropdown.grid(column=1, row=1)




        """# Create a frame for the Dispaly Stocks button
        displayStocksFrame = tk.Frame(self)
        displayStocksFrame.grid(column=0, row=0)

        # Create the lable for Display Stocks
        displayStocksLabel = tk.Label(displayStocksFrame, text="Display Stocks: ")
        displayStocksLabel.grid(column=0, row=0)

        # Create the Display Stocks button
        displayStocks = tk.Button(displayStocksFrame, text="Display Stocks", bg="lightblue")
        displayStocks.grid(column=1, row=0)

        # Create the menu for backtesting
        menu = tk.StringVar()
        menu.set("Backtesting Options")

        # The options to choose from
        options = ["Strategy 1", "Strategy 2"]

        # This gets the strategy selected by the user
        def getStrategy(self):

            print(menu.get())

        # Create a label widget for the user to see the name of the dropdown
        strategyInfo = tk.Label(self, text="Strategy Type: ")
        strategyInfo.grid(column=1, row=0)

        # Create the information to be displayed in the dropdown
        dropDown = tk.OptionMenu(self, menu, *options, command=getStrategy)
        dropDown.config(bg="lightgray")
        dropDown.grid(column=1, row=0)

        # Create the Show Profile button
        displayStocks = tk.Button(self, text="Display Portfolio", bg="lightgreen")
        displayStocks.grid(column=2, row=0)"""

    def create_portfolio(self):

        # Create the portfolio frame beneath the stock data
        portfolioFrame = tk.Frame(self)
        portfolioFrame.grid(column=1, row=3)

        # Create a button "My Portfolio" for accessing the portfolio
        # TODO: Connect this button to another window when clicked
        portfolioButton = tk.Button(portfolioFrame, text="My Portfolio")
        portfolioButton.config(bg="lightgreen")

        # pady=(top padding, bottom padding)
        portfolioButton.grid(column=0, row=0, pady=(0, 60))


if __name__ == "__main__":

    # Create an instance of our app
    app = DisplayClass()

    # This function displays the app to the screen
    app.mainloop()
