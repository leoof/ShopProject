# Imports the Tkinter module
import tkinter
from tkinter import *
from login import LoginApp

class HomeScreen:
    def __init__(self, app):
        self.app = app
        self.label = Label(self.app,
                           text="BREAD BANK - WE SELL BREAD, WE SELL LOAFS",
                           font=('Helvetica', 9, 'bold'))
        self.label.pack()
        self.loginButton = Button(self.app, text="Admin", command=self.login)
        self.loginButton.pack()
        self.shopButton = Button(self.app, text="Start your shop", command=self.startShop)
        self.shopButton.pack()

    def login(self):
      self.app.destroy()
      root1 = Tk()
      root1.title("Shop")
      root1.geometry("775x420")
      app1 = LoginApp(root1)
      root1.mainloop()

    def startShop(
      
JJ = bad
print(JJ)



if __name__ == "__main__":  # The loop that creates the windows and keeps it running
    root = Tk()
    root.title("Shop")
    root.geometry("350x275")
    app = HomeScreen(root)
    root.mainloop()
