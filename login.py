# Imports the Tkinter module
import tkinter
from tkinter import *

# A class that will be used to setup the shop functions
class LoginApp:
    def __init__(self, app):
        self.username = "admin"
        self.password = "password"
        self.app = app

        self.l1 = Label(self.app,
                        text="BREAD BROTHER LOGIN TO BUY SOME BREAD BROTHER",
                        font=('Helvetica', 15, 'bold'))
        self.l1.pack()
        self.N1 = Label(self.app, text="Username")
        self.N1.pack()
        self.E1 = Entry(self.app, width=30)
        self.E1.pack()
        self.L2 = Label(self.app, text="Password")
        self.L2.pack()
        self.E2 = Entry(self.app, width=30, show="•")
        self.E2.pack()
        self.L3 = Label(self.app, text=" ")

        # Buttons that launch the commands
        self.B1 = Button(self.app,
                         text="Login",
                         command=self.verification,
                         font=('Comic Sans MS', 16)).pack(side=tkinter.BOTTOM)

    # An verification function
    def verification(self):           
        if self.E1.get() == self.username:
            if self.E2.get() == self.password:
                self.L3 = Label(self.app, text="WELCOME BREAD BROTHER")
                self.L3.pack(side=BOTTOM)              
                self.app.destroy()
                self.app1 = Tk()
                self.app1.title("Shop")
                self.app1.geometry("775x400")
                app1 = HomeScreen(self.app1)
                self.app1.mainloop()
                
            else:
                self.L3.config(text="YOU ARE NOT A BREAD BROTHER LEAVE BROTHER NOW BROTHER")
                self.L3.pack(side=BOTTOM)
        else:
            self.L3.config(text="YOU ARE NOT A BREAD BROTHER LEAVE BROTHER NOW BROTHER")
            self.L3.pack(side=BOTTOM)
