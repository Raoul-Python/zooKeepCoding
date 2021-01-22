from tkinter import *
from tkinter import ttk


class mainApp(Tk): #La clase mainApp() hereda de la clase Tk()

    size = "800x500"

    def __init__(self):
        #Invoco el contructor de Tk()
        Tk.__init__(self)

        self.geometry(self.size)
        self.title("Mi Window´s")
        self.configure(bg = "Blue")

    def inicio(self):
        self.mainloop()
    
    
    
if __name__ == "__main__":
    app = mainApp() #Creo objeto clase mainApp()
    app.inicio()
