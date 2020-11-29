import tkinter as tk
from tkinter import *
import csv
import pandas as pd
from tkinter import ttk

df = pd.read_csv("cardiocases.csv") ## using pandas to make the csv a dataframe

root = tk.Tk() ## create window
root.title('Supersquad') ## title of window

lbl = Label(root, text = "Please select a Risk to view associated patients") ## adding a label to display above drop down
lbl.pack()

options = ['low','mild','moderate','moderate high','high','major'] ## drop down menu options

variable = tk.StringVar()
variable.set(options[0]) ## default display upon opening
    
opt = tk.OptionMenu(root, variable, *options) 
opt.configure(font=("Arial",20)) ## making the drop down very visable
opt.pack() ## .pack() makes things show up in the window


## making the function command for thisbutton, using the drop down choice to make a new data frame to dispaly in Treeview
def retrieve():
    sift = df.loc[df['Risk'] == (variable.get())]
    cols = list(sift.columns)
    tree["columns"] = cols
    for i in cols:
        tree.column(i, anchor="w")
        tree.heading(i, text=i, anchor='w')

        for index, row in sift.iterrows():
            tree.insert("",0,text=index,values=list(row))
    
## making a button named Retrieve Patients
thisbutton = Button(root, text="Retrieve Patients", command = retrieve)
thisbutton.pack()

frame1 = tk.LabelFrame(root, text="Patients") ## a frame is needed to put Treeview and Scrollbars together
frame1.pack()

## setting up Treeview for dataframe results
tree = ttk.Treeview(frame1)
treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tree.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tree.xview) # command means update the xaxis view of the widget
tree.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget
tree.pack()  

root.mainloop()