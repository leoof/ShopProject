# Imports the Tkinter module
import tkinter
from tkinter import *

class HomeScreen:
  def __init__(self, app):
    self.app = app

    self.label = Label(self.app, text="BREAD BANK - WE SELL BREAD, WE SELL LOAFS",font=('Arial'))
    self.label.pack()
    B1 = Button(self.app, text="Login", command=self.login)
    self.B1.pack()

  def login():
    if __name__ == '__name__':
      root.destroy()
      root1 = Tk()
      root1.title("Shop")
      root1.geometry("450x275")
      app1 = HomeScreen(root1)
      root1.mainloop()

