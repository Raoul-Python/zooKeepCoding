from tkinter import *
from tkinter import ttk


class mainApp():

    size = "800x500"

    def __init__(self):
        self.root = Tk()#creo un objeto de la clase Tk() dentro de la clase mainApp()
        self.root.geometry(self.size)
        self.root.title("Mi Window´s")
        self.root.configure(bg = "Blue")

    def inicio(self):
        self.root.mainloop()
    
    
    
if __name__ == "__main__":
    app = mainApp() #Creo objeto clase mainApp()
    app.inicio()
