# Imports the Tkinter module
import tkinter
from tkinter import *
from homeScreen import HomeScreen

global root
root = Tk()


# A class that will be used to setup the calculator functions
class MainClass:
    def __init__(self, app):
        self.verified = 0
        self.username = "admin"
        self.password = "password"
        self.app = app

        self.l1 = Label(root,
                        text="BREAD BANK - WE SELL BREAD, WE SELL LOAFS",
                        font=('Helvetica', 9, 'bold'))
        self.l1.pack()
        self.N1 = Label(root, text="Username")
        self.N1.pack()
        self.E1 = Entry(root, width=30)
        self.E1.pack()
        self.L2 = Label(root, text="Password")
        self.L2.pack()
        self.E2 = Entry(root, width=30, show="•")
        self.E2.pack()
        self.L3 = Label(root, text=" ")

        # Buttons that launch the commands
        self.B1 = Button(root,
                         text="Login",
                         command=self.verification,
                         font=('Comic Sans MS', 16)).pack(side=tkinter.BOTTOM)

    # An verification function
    def verification(self):
        if self.E1.get() == self.username:
            if self.E2.get() == self.password:
                self.L3 = Label(root, text="Login successful, welcome!")
                self.L3.pack(side=BOTTOM)
                self.verified = 1
                root.quit()
                root1 = Tk()
                root1.title("Shop")
                root1.geometry("350x275")
                app1 = HomeScreen(root1)
                root.mainloop()
                
            else:
                self.L3.config(text="Username or password is incorrect.")
                self.L3.pack(side=BOTTOM)
        else:
            self.L3.config(text="Username or password is incorrect.")
            self.L3.pack(side=BOTTOM)


if __name__ == "__main__":  # The loop that creates the windows and keeps it running
    root = Tk()
    root.title("Shop")
    root.geometry("350x275")
    app = MainClass(root)
    root.mainloop()
