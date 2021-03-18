# Imports the Tkinter module
import tkinter
from tkinter import *

class HomeScreen:
  def __init__(self, app):
    self.app = app

    self.label = Label(self.app, text="Hi")
    self.label.pack()

