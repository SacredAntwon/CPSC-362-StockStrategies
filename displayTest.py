import tkinter as tk
import tkinter.font as tkFont

# THIS CLASS IS FOR TESTING PURPOSES ONLY FOR DRAG-N-DROP FUNCTIONALITY!

class App:
    def __init__(self, root):
        #setting title
        root.title("Our project")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_420=tk.Button(root)
        GButton_420["bg"] = "#01aaed"
        GButton_420["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=10)
        GButton_420["font"] = ft
        GButton_420["fg"] = "#90ee90"
        GButton_420["justify"] = "center"
        GButton_420["text"] = "Display stocks"
        GButton_420["relief"] = "flat"
        GButton_420.place(x=130,y=80,width=87,height=39)
        GButton_420["command"] = self.GButton_420_command

        backtesting = ('A', 'B', 'C', 'D')
        backtesting_var = tk.StringVar(value = backtesting)

        GListBox_283=tk.Listbox(root)
        GListBox_283["bg"] = "#01aaed"
        GListBox_283["borderwidth"] = "1px"
        GListBox_283["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_283["font"] = ft
        GListBox_283["fg"] = "#90ee90"
        GListBox_283["justify"] = "center"
        GListBox_283["relief"] = "groove"
        GListBox_283.place(x=240,y=80,width=100,height=65)
        GListBox_283["exportselection"] = "1"
        GListBox_283["listvariable"] = backtesting_var
        GListBox_283["selectmode"] = "browse"

        GButton_187=tk.Button(root)
        GButton_187["bg"] = "#01aaed"
        GButton_187["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        GButton_187["font"] = ft
        GButton_187["fg"] = "#90ee90"
        GButton_187["justify"] = "center"
        GButton_187["text"] = "Show profile"
        GButton_187["relief"] = "flat"
        GButton_187.place(x=360,y=80,width=93,height=40)
        GButton_187["command"] = self.GButton_187_command

        GLabel_61=tk.Label(root)
        GLabel_61["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_61["font"] = ft
        GLabel_61["fg"] = "#90ee90"
        GLabel_61["justify"] = "center"
        GLabel_61["text"] = "stock project"
        GLabel_61["relief"] = "flat"
        GLabel_61.place(x=240,y=20,width=101,height=40)

        GButton_504=tk.Button(root)
        GButton_504["bg"] = "#01aaed"
        GButton_504["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        GButton_504["font"] = ft
        GButton_504["fg"] = "#90ee90"
        GButton_504["justify"] = "center"
        GButton_504["text"] = "Add to portfolio"
        GButton_504["relief"] = "flat"
        GButton_504.place(x=240,y=430,width=123,height=30)
        GButton_504["command"] = self.GButton_504_command

    def GButton_420_command(self):
        print("command")


    def GButton_187_command(self):
        print("command")


    def GButton_504_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()