import tkinter as tk
from tkinter import *
import csv
from tkinter import ttk

patients = []
header = []

with open("cardiocases.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    header = next(reader, None)
    for row in reader:
        patients.append(row)  ##  All the above lines are from Jin's GUI code

root = tk.Tk() ## create window
root.title('Supersquad') ## title of window

lbl = Label(root, text = "Please select a Risk to view associated patients") ## adding a label to display above drop down
lbl.pack()

options = ['low','mild','moderate','moderate high','high','major']

variable = tk.StringVar()
variable.set(options[0]) ## displays when first runs, before user selection
    
opt = tk.OptionMenu(root, variable, *options)
opt.configure(font=("Arial",20)) ## making the drop down very visable
opt.pack() ## .pack() makes things show up in the gui

a_frame = Frame(root) ## scrollbar and text box require frame to wrok together
a_frame.pack()

xscrollbar = Scrollbar(a_frame,orient = HORIZONTAL) ## horizontal scroll bar (x)
xscrollbar.pack(side = BOTTOM, fill = X)

yscrollbar = Scrollbar(a_frame)  ## vertical scroll bar (y)
yscrollbar.pack(side = RIGHT, fill = Y)

 ## text box to display results
T = tk.Text(a_frame, wrap = NONE, yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
T.pack()

xscrollbar.config(command=T.xview)
yscrollbar.config(command=T.yview)

def retrieve():
   for p in patients:    ## defining the command thisbutton uses
       for p in patients:
           if p[20] == variable.get():
               T.insert(tk.END,p)


## making a button named Retrieve Patients
thisbutton = Button(root, text="Retrieve Patients", command = retrieve)
thisbutton.pack()

## a button to close the results window
done = Button(root, text = "Close", command = root.destroy)
done.pack()

root.mainloop()