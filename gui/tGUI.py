import tkinter as tk
from tkinter import *
import csv
from tkinter import ttk

patients = []
header = []

with open("patients.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    header = next(reader, None)
    for row in reader:
        patients.append(row)  ##  All the above lines are from Jin's GUI code

window = tk.Tk() ## create window
window.title = ('Supersquad') ## title of window

lbl = Label(window, text = "Please select a Risk to view patients") ## adding a label to display above drop down
lbl.grid(column=0, row=0) ## positioning the label
lbl.pack()

options = ['low','mild','moderate','moderate high','high','major']

variable = tk.StringVar()
variable.set(options[0]) ## displays when first runs, before user selection
    
opt = tk.OptionMenu(window, variable, *options)
opt.pack() ## .pack() makes things show up in the gui

tk.Text(root, height=10, width=50). ## John's code
T = tk.Text(root, height=10, width=50). ## John's code
T.pack(). ## John's code

def retrieve():   ## defining the command thisbutton uses
    for p in patients:
        if p[20] == variable.get():
                        
## making a button named Retrieve Patients
thisbutton = Button(window, text="Retrieve Patients", command = retrieve)
thisbutton.pack()


window.mainloop()
