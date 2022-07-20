import tkinter as tk
from tkinter import ttk


class DisplayClass(tk.Tk):

    # This initializer places all widgets within their corresponding frame
    def __init__(self):
        super().__init__()

        #self.geometry("240x100")
        self.geometry("1280x720")
        self.title('Login')
        # self.resizable(0, 0)

        # configure the grid
        # self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weight=3)

        self.create_stockinfo()

    # This function creates the widgets for all stock info
    def create_stockinfo(self):

        # Create the underlying frame that holds all stock information
        stockInfo = ttk.Frame(self)
        stockInfo.grid(column=0, row=0)

        categories = ["Stock", "Open", "Close", "Bid", "Ask", "Vol", "PE", "EPS", "Firm", "Brade", "BT%"]

        for index in range(len(categories)):

            # Create the "stock" name inside the stockInfo frame
            stockName = ttk.Label(stockInfo, text=categories[index])
            stockName.grid(column=index, row=0)

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