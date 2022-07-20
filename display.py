import tkinter as tk
from tkinter import ttk


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
        stockDict = {'AAPL': {'regularMarketOpen': 151.12, 'regularMarketPreviousClose': 151.0, 'bid': 152.4, 'ask': 152.45, 'regularMarketVolume': 63805728, 'trailingPE': 24.884552, 'epsTrailingTwelveMonths': 6.15, 'averageAnalystRating': '1.9 - Buy'}, 'AMGN': {'regularMarketOpen': 246.7, 'regularMarketPreviousClose': 247.32, 'bid': 246.97, 'ask': 246.59, 'regularMarketVolume': 2057471, 'trailingPE': 24.346497, 'epsTrailingTwelveMonths': 10.13, 'averageAnalystRating': '2.6 - Hold'}, 'AXP': {'regularMarketOpen': 146.87, 'regularMarketPreviousClose': 147.78, 'bid': 149.03, 'ask': 149.03, 'regularMarketVolume': 2290800, 'trailingPE': 14.87812, 'epsTrailingTwelveMonths': 10.01, 'averageAnalystRating': '2.3 - Buy'}, 'BA': {'regularMarketOpen': 156.0, 'regularMarketPreviousClose': 156.13, 'bid': 157.15, 'ask': 157.28, 'regularMarketVolume': 8644291, 'trailingPE': None, 'epsTrailingTwelveMonths': -8.285, 'averageAnalystRating': None}, 'CAT': {'regularMarketOpen': 178.78, 'regularMarketPreviousClose': 179.49, 'bid': 180.13, 'ask': 180.17, 'regularMarketVolume': 2088910, 'trailingPE': 15.098154, 'epsTrailingTwelveMonths': 11.92, 'averageAnalystRating': '2.4 - Buy'}, 'CRM': {'regularMarketOpen': 176.1, 'regularMarketPreviousClose': 173.81, 'bid': 181.5, 'ask': 182.0, 'regularMarketVolume': 5601122, 'trailingPE': 173.76192, 'epsTrailingTwelveMonths': 1.05, 'averageAnalystRating': '1.8 - Buy'}, 'CSCO': {'regularMarketOpen': 44.08, 'regularMarketPreviousClose': 44.03, 'bid': 44.16, 'ask': 44.12, 'regularMarketVolume': 15596380, 'trailingPE': 15.484211, 'epsTrailingTwelveMonths': 2.85, 'averageAnalystRating': '2.5 - Buy'}, 'CVX': {'regularMarketOpen': 144.5, 'regularMarketPreviousClose': 144.61, 'bid': 146.0, 'ask': 146.53, 'regularMarketVolume': 7521261, 'trailingPE': 13.770677, 'epsTrailingTwelveMonths': 10.64, 'averageAnalystRating': '2.4 - Buy'}, 'DIS': {'regularMarketOpen': 100.25, 'regularMarketPreviousClose': 99.61, 'bid': 103.0, 'ask': 103.4, 'regularMarketVolume': 13679452, 'trailingPE': 67.11039, 'epsTrailingTwelveMonths': 1.54, 'averageAnalystRating': '2.0 - Buy'}, 'DOW': {'regularMarketOpen': 52.45, 'regularMarketPreviousClose': 52.45, 'bid': 52.4, 'ask': 52.7, 'regularMarketVolume': 5973422, 'trailingPE': 5.7306433, 'epsTrailingTwelveMonths': 9.17, 'averageAnalystRating': '2.7 - Hold'}, 'GS': {'regularMarketOpen': 317.28, 'regularMarketPreviousClose': 318.05, 'bid': 321.43, 'ask': 321.0, 'regularMarketVolume': 3475882, 'trailingPE': 7.2594857, 'epsTrailingTwelveMonths': 44.28, 'averageAnalystRating': '2.2 - Buy'}, 'HD': {'regularMarketOpen': 300.93, 'regularMarketPreviousClose': 299.83, 'bid': 301.82, 'ask': 302.3, 'regularMarketVolume': 2532233, 'trailingPE': 19.18147, 'epsTrailingTwelveMonths': 15.76, 'averageAnalystRating': '2.1 - Buy'}, 'HON': {'regularMarketOpen': 176.81, 'regularMarketPreviousClose': 177.23, 'bid': 177.22, 'ask': 180.0, 'regularMarketVolume': 1640193, 'trailingPE': 23.704786, 'epsTrailingTwelveMonths': 7.52, 'averageAnalystRating': '2.3 - Buy'}, 'IBM': {'regularMarketOpen': 130.7, 'regularMarketPreviousClose': 130.88, 'bid': 128.75, 'ask': 128.98, 'regularMarketVolume': 9864151, 'trailingPE': 21.215303, 'epsTrailingTwelveMonths': 6.089, 'averageAnalystRating': '2.7 - Hold'}, 'INTC': {'regularMarketOpen': 40.21, 'regularMarketPreviousClose': 40.22, 'bid': 40.35, 'ask': 40.57, 'regularMarketVolume': 35504766, 'trailingPE': 6.7375417, 'epsTrailingTwelveMonths': 6.02, 'averageAnalystRating': '2.9 - Hold'}, 'JNJ': {'regularMarketOpen': 172.2, 'regularMarketPreviousClose': 171.69, 'bid': 170.21, 'ask': 170.66, 'regularMarketVolume': 7447714, 'trailingPE': 23.006739, 'epsTrailingTwelveMonths': 7.42, 'averageAnalystRating': '2.3 - Buy'}, 'JPM': {'regularMarketOpen': 114.1, 'regularMarketPreviousClose': 114.56, 'bid': 114.01, 'ask': 114.51, 'regularMarketVolume': 10495520, 'trailingPE': 9.185245, 'epsTrailingTwelveMonths': 12.47, 'averageAnalystRating': '2.3 - Buy'}, 'KO': {'regularMarketOpen': 62.4, 'regularMarketPreviousClose': 62.53, 'bid': 61.51, 'ask': 61.52, 'regularMarketVolume': 10995484, 'trailingPE': 25.949368, 'epsTrailingTwelveMonths': 2.37, 'averageAnalystRating': '2.2 - Buy'}, 'MCD': {'regularMarketOpen': 256.78, 'regularMarketPreviousClose': 256.5, 'bid': 253.8, 'ask': 255.0, 'regularMarketVolume': 2179844, 'trailingPE': 26.882788, 'epsTrailingTwelveMonths': 9.47, 'averageAnalystRating': '2.0 - Buy'}, 'MMM': {'regularMarketOpen': 132.12, 'regularMarketPreviousClose': 132.13, 'bid': 132.99, 'ask': 133.5, 'regularMarketVolume': 1920839, 'trailingPE': 13.840791, 'epsTrailingTwelveMonths': 9.61, 'averageAnalystRating': '3.3 - Hold'}, 'MRK': {'regularMarketOpen': 92.36, 'regularMarketPreviousClose': 92.36, 'bid': 89.89, 'ask': 89.74, 'regularMarketVolume': 11646268, 'trailingPE': 16.35949, 'epsTrailingTwelveMonths': 5.48, 'averageAnalystRating': '2.2 - Buy'}, 'MSFT': {'regularMarketOpen': 259.9, 'regularMarketPreviousClose': 259.53, 'bid': 261.0, 'ask': 261.38, 'regularMarketVolume': 22337896, 'trailingPE': 27.376825, 'epsTrailingTwelveMonths': 9.58, 'averageAnalystRating': '1.7 - Buy'}, 'NKE': {'regularMarketOpen': 109.22, 'regularMarketPreviousClose': 109.19, 'bid': 111.21, 'ask': 111.22, 'regularMarketVolume': 5880860, 'trailingPE': 29.629333, 'epsTrailingTwelveMonths': 3.75, 'averageAnalystRating': '2.1 - Buy'}, 'PG': {'regularMarketOpen': 144.0, 'regularMarketPreviousClose': 144.04, 'bid': 141.98, 'ask': 141.82, 'regularMarketVolume': 8158270, 'trailingPE': 24.746506, 'epsTrailingTwelveMonths': 5.72, 'averageAnalystRating': '2.4 - Buy'}, 'TRV': {'regularMarketOpen': 158.43, 'regularMarketPreviousClose': 158.35, 'bid': 154.43, 'ask': 165.53, 'regularMarketVolume': 1270917, 'trailingPE': 10.031705, 'epsTrailingTwelveMonths': 15.77, 'averageAnalystRating': '2.9 - Hold'}, 'UNH': {'regularMarketOpen': 533.45, 'regularMarketPreviousClose': 533.45, 'bid': 517.5, 'ask': 528.38, 'regularMarketVolume': 3615531, 'trailingPE': 27.140543, 'epsTrailingTwelveMonths': 19.14, 'averageAnalystRating': '1.8 - Buy'}, 'V': {'regularMarketOpen': 212.0, 'regularMarketPreviousClose': 213.66, 'bid': 213.0, 'ask': 213.45, 'regularMarketVolume': 4456765, 'trailingPE': 33.496075, 'epsTrailingTwelveMonths': 6.37, 'averageAnalystRating': '1.8 - Buy'}, 'VZ': {'regularMarketOpen': 50.47, 'regularMarketPreviousClose': 50.45, 'bid': 49.15, 'ask': 49.11, 'regularMarketVolume': 28191664, 'trailingPE': 9.546693, 'epsTrailingTwelveMonths': 5.14, 'averageAnalystRating': '2.7 - Hold'}, 'WBA': {'regularMarketOpen': 38.58, 'regularMarketPreviousClose': 38.6, 'bid': 38.66, 'ask': 38.92, 'regularMarketVolume': 4807536, 'trailingPE': 6.5966096, 'epsTrailingTwelveMonths': 5.9, 'averageAnalystRating': '3.1 - Hold'}, 'WMT': {'regularMarketOpen': 130.51, 'regularMarketPreviousClose': 129.56, 'bid': 130.0, 'ask': 130.45, 'regularMarketVolume': 6186306, 'trailingPE': 28.155172, 'epsTrailingTwelveMonths': 4.64, 'averageAnalystRating': '1.9 - Buy'}}
        stockNames = ['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS', 'DOW', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH', 'V', 'VZ', 'WBA', 'WMT']

        # Create the underlying frame that holds all stock information
        stockInfo = tk.Frame(self)
        stockInfo.grid(column=1, row=1)

        categories = ["Stock", "Open", "Close", "Bid", "Ask", "Vol", "PE", "EPS", "Firm", "Brade", "BT%"]
        for index in range(len(categories)):

            # Create each category inside the stockInfo frame
            stockName = tk.Label(stockInfo, text=categories[index], font='Verdana 13 underline')
            stockName.grid(column=index, row=0)

            # Add here the displays for each stock retrieved from the API call
            

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