import tkinter
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

        tabControl.add(tab1, text='Employees')
        tabControl.add(tab2, text='Randomizer')
        tabControl.add(tab3, text='Setting')
        tabControl.add(tab4, text='Info')

        tabControl.pack(expand=1,fill="both")
        ttk.Label(tab2,
                  text="Randomize list").grid(column=0,
                                              row=0,
                                              padx=30,
                                              pady=30)
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

        tv = ttk.Treeview(tab1,
                          columns=(1 , 2, 3, 4),
                          show='headings',
                          height=8)
        tab1.grid_columnconfigure(0, weight=1)
        tab1.grid_rowconfigure(0, weight=1)
        tv.grid(column=0,row=0,padx=5,pady=5,sticky=N+E+W)

        tv.heading(1, text="Id")
        tv.column(1,width=20, minwidth=5)
        tv.heading(2, text="Name")
        tv.column(2, width=100, minwidth=50)
        tv.heading(3, text="Day of birth")
        tv.column(3, width=100)
        tv.heading(4, text="Student status")
        tv.column(4, width=50)

        add_employee_button = tkinter.Button(tab1, text="Add new employee")
        add_employee_button.grid()

    def run(self):
        WINDOW_WIDTH = 600
        WINDOW_HEIGHT = 500
        POSITION_RIGHT = 800
        POSITION_DOWN = 300
        self.root.title("CMGT center")
        self.root.geometry(f"{WINDOW_WIDTH}x"
                           f"{WINDOW_HEIGHT}+"
                           f"{POSITION_RIGHT}+"
                           f"{POSITION_DOWN}")
        self.root.mainloop()




#CONFIG

app = App()
app.run()
