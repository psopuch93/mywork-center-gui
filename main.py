from tkinter import *
from tkinter import ttk

import tkinter as tk

class App():

    def __init__(self):
        self.root = tk.Tk()

        tabControl = ttk.Notebook(self.root)
        tab1 = ttk.Frame(self.root)
        tab2 = ttk.Frame(self.root)
        tab3 = ttk.Frame(self.root)
        tab4 = ttk.Frame(self.root)

        tabControl.add(tab1, text = 'Employees')
        tabControl.add(tab2, text= 'Randomizer')
        tabControl.add(tab3, text='Setting')
        tabControl.add(tab4, text='Info')

        tabControl.pack(expand = 1, fill="both")

        ttk.Label(tab1,
                  text="Employees list").grid(column = 0,
                                              row = 0,
                                              padx = 30,
                                              pady = 30)
        ttk.Label(tab2,
                  text="Randomize list").grid(column = 0,
                                              row = 0,
                                              padx = 30,
                                              pady = 30)
        ttk.Label(tab3,
                  text="Settings").grid(column=0,
                                              row=0,
                                              padx=30,
                                              pady=30)
        ttk.Label(tab4,
                  text="Info here").grid(column=0,
                                        row=0,
                                        padx=30,
                                        pady=30)

    def run(self):
        WINDOW_WIDTH = 600
        WINDOW_HEIGHT = 500
        POSITION_RIGHT = 800
        POSITION_DOWN = 300
        self.root.title("CMGT center")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{POSITION_RIGHT}+{POSITION_DOWN}")
        self.root.mainloop()



#CONFIG




app = App()
app.run()
