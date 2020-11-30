import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv
import random
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import pandas as pd

#importing the modules
from patient_cardiovascular import patient_cardiovascular
from statistics import statistics

'''JIN'S CODE'''

# make a patient id generator which is protected
def _makeIDGen():
    i = 1
    while True:
        yield i
        i += 1
# create a generator, and can use the same instance for every new Patient 
_idGen = _makeIDGen()
# a protected list of states
_stateset1 = ['Utah', 'Texas', 'Ohio', 'California', 'Idaho', 'Maine', 'Alaska', 'Colorado', 'North Carolina', 'New York']
# a protected list of visittypes
_visittype = ['primary care', 'specialist', 'hospital inpatient', 'emergency', 'nursing facility']
# a protected dictionary of heights, key is height in inches while the value is a tuple of weight ranges (min, max)
_heights = {
    58: (91, 186), 
    59: (94, 193), 
    60: (97, 199), 
    61: (100, 206), 
    62: (104, 213), 
    63: (107, 220), 
    64: (110, 227), 
    65: (114, 234), 
    66: (118, 241), 
    67: (121, 249), 
    68: (125, 256),
    69: (128, 263), 
    70: (132, 271), 
    71: (136, 279), 
    72: (140, 287), 
    73: (144, 295), 
    74: (148, 303), 
    75: (152, 311), 
    76: (156, 320)
}
# a protected dictionary of vitalsigns, keys are different groups based on age range, the value is another dictionary.
# In the sub dictionaries, the keys are different vitalsigns, and the values are tuple with range for that vital sign.
_vital_signs = {
    "child1": {
        "heartrate": (70, 120),
        "respiration": (20, 30),
        "blood pressure": ((90, 110), (55, 75)),
        "temperature": (97.4, 99.6)
    },
    "child2": {
        "heartrate": (70, 120),
        "respiration": (12, 20),
        "blood pressure": ((90, 110), (55, 75)),
        "temperature": (97.4, 99.6)
    },
    "adult": {
        "heartrate": (60, 100),
        "respiration": (12, 18),
        "blood pressure": ((110, 135), (65, 85)),
        "temperature": (97.4, 99.6)
    }
}
# class named Patient, and use __init__ to initiate attributes under the class, using random values
class Patient:
    def __init__(self):
        # use global in case if there's assigned height, then BMI vlaue can change based on the assigned value
        global _heights 

        # use next to iterate generator of yield, ID starts at 1
        self.id =  next(_idGen) 

        # generate random provider ID include start and end
        self.provider = random.randint(1, 10) 
        
        # generate random age include start and end
        self.age = random.randint(1, 100)  
        
        # randomly choose F or M
        self.sex = random.choice('FM')  
        
        # randomly choose from stateset1
        self.state = random.choice(_stateset1)   
        
        # randomly choose from visittype
        self.visittype = random.choice(_visittype)  
        
        # randomly choose from the keys in height dictionary, those keys were put in a list 
        self.height = random.choice(list(_heights.keys())) 
        
        # get the value from chosen key name(use self.height), and use * to unpack the value in tuple. Finally use randint to generate a random weight
        self.weight = random.randint(*_heights[self.height])  

        # to know which age is in which key in vitalsigns
        if self.age >= 1 and self.age < 6:   
            key = "child1"
        elif self.age >= 6 and self.age < 12:
            key = "child2"
        else:
            key = "adult"

        # vs is the vitalsigns dictionary based on which key was chosen 
        vs = _vital_signs[key]
        
        # key in vs dictionary, and use * to unpack the value in the tuple, finally use randint to generate data
        self.heart_rate = random.randint(*vs["heartrate"])   
        self.respiration = random.randint(*vs["respiration"])
        
        # index 0 for the first tuple, index 1 for the second tuple
        self.blood_pressure = (random.randint(*vs["blood pressure"][0]), random.randint(*vs["blood pressure"][1]))
        self.temperature = random.uniform(*vs["temperature"])

    # bmi definition to calculate bmi for USA units 
    def bmi(self):
        return self.weight * 703 / self.height ** 2

    # definition to convert inches to ft and inch
    def height_to_ftin(self):
        ft, inch = divmod(self.height, 12)
        return "{}' {}\"".format(ft, inch)

    # use def __str__ for a string representation of this object
    def __str__(self):
        return f'ID: {self.id}, Provider: {self.provider}, Age: {self.age}, Sex: {self.sex}, State: {self.state}, Visit_type: {self.visittype}, Weight: {self.weight}, Height: {self.height_to_ftin()}, BMI: {self.bmi()}, Heart Rate: {self.heart_rate} bpm, Respiration: {self.respiration} bpm, Blood Pressure: {self.blood_pressure[0]}/{self.blood_pressure[1]} mmHg, Temperature: {self.temperature:.2f}\n'

    # use def __repr__ and str(self) present the items in the patients list as string
    def __repr__(self):
        return str(self)

# create an empty patients list
patients = []
# create 300 patients by using Patient class in patient module
for i in range(0, 300):
    p = Patient()
    patients.append(p)

# print the whole list, the items in the patients list are all patient.Patient
# print(patients)

with open('patients.csv', 'w', newline='') as file:
    # writer for writing the csv rows in the file
    w = csv.writer(file)
    # use writerow to write the header in csv file
    w.writerow(['id', 'provider', 'age', 'sex', 'state', 'visittype', 'weight', 'height', 'bmi', 'heartrate', 'respiration', 'systolic blood pressure', 'diastolic blood pressure', 'temperature'])
    # write every patient to the csv file
    for p in patients:
        w.writerow([p.id, p.provider, p.age, p.sex, p.state, p.visittype, p.weight, p.height, p.bmi(), p.heart_rate, p.respiration, p.blood_pressure[0], p.blood_pressure[1], "{:.2f}".format(p.temperature)])
file.close()

'''JIN'S GUI CODE'''

patients = []
header = []

with open("patients.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    header = next(reader, None)
    for row in reader:
        patients.append(row)

root = tk.Tk()
# adjust the window's size
root.geometry("400x240")
#change the window's title
root.wm_title("Supersquad")
# create patinet ID label, w is the label
w = tk.Label(root, text="Patient ID")
# use pack to determine the size of the label
w.pack()
# create the text box
patientid = tk.Text(root, height=1, width=10)
# use pack to determine the size of the text (another widget)
patientid.pack()
# create a function which can print what the user types for patientid
def find_patient():
    for p in patients:
        if p[0] == patientid.get(1.0, tk.END+"-1c"):
            def dismiss ():
                dlg.grab_release()
                dlg.destroy()
            # create another new window
            dlg = tk.Toplevel(root)
            # the name of the new window
            dlg.wm_title("Patinet %s Information" % p[0])
            # show the patient's providerID
            proid = tk.Label(dlg, text="Provider ID")
            proid.pack()
            provid = tk.Text(dlg, height=1, width=10)
            provid.insert(tk.END, p[1])
            provid.pack()

            # show patient's age
            page = tk.Label(dlg, text="Age")
            page.pack()
            age = tk.Text(dlg, height=1, width=10)
            age.insert(tk.END, p[2])
            age.pack()

            # show patient's sex
            sex = tk.Label(dlg, text="Sex")
            sex.pack()
            # Holds a string
            v = StringVar(dlg)
            v.set(p[3])
            # Dictionary to create multiple buttons 
            Radiobutton(dlg, text = "Male", variable = v, value = "M").pack(side = TOP, ipady = 5)
            Radiobutton(dlg, text = "Female", variable = v, value = "F").pack(side = TOP, ipady = 5)
            
            # show patient's state
            pstate = tk.Label(dlg, text="State")
            pstate.pack()
            state = tk.Text(dlg, height=1, width=15)
            state.insert(tk.END, p[4])
            state.pack()

            # show patient's vt
            pvt = tk.Label(dlg, text="Visit Type")
            pvt.pack()
            # Create a Tkinter variable
            vt = StringVar(dlg)
            vtchoosen = ttk.Combobox(dlg, width = 27,  textvariable = vt) 
            # Adding combobox drop down list
            vtchoosen['values'] = ('primary care', 'specialist', 'hospital inpatient', 'emergency', 'nursing facility')
            # set the default option
            vtchoosen.current(0)
            vtchoosen.pack()

            # create the text box, can edit the height if the patient's height changes
            def cal_bmi(e):
                try:
                    h = float(pheight.get(1.0, tk.END+"-1c"))
                    w = float(pweight.get(1.0, tk.END+"-1c"))
                    bmivalue.set("{bmi:.2f}".format(bmi=w*703/h**2))
                except:
                    pass

            # show patient's height
            pheigh = tk.Label(dlg, text="Height (in)")
            pheigh.pack()

            pheight = tk.Text(dlg, height=1, width=10)
            pheight.insert(tk.END, p[7])
            pheight.bind("<KeyRelease>", cal_bmi)
            pheight.pack()

            # show patient's weight 
            pweigh = tk.Label(dlg, text="Weight (lb)")
            pweigh.pack()
            # create the text box, can edit the weight if the patient's weight changes
            pweight = tk.Text(dlg, height=1, width=10)
            pweight.insert(tk.END, p[6])
            pweight.bind("<KeyRelease>", cal_bmi)
            pweight.pack()

            # show patient's bmi
            pbmi = tk.Label(dlg, text="BMI")
            pbmi.pack()
            bmivalue = tk.StringVar()
            bmivaluel = tk.Label(dlg, textvariable=bmivalue)
            bmivaluel.pack()
            cal_bmi(None)

            # show patient's vital signs
            pvitalsigns = tk.Label(dlg, text="Vital Signs")
            pvitalsigns.pack()
            pheartrate = tk.Label(dlg, text="Heart rate")
            pheartrate.pack()
            heartrate = tk.Text(dlg, height=1, width=10)
            heartrate.insert(tk.END, p[9])
            heartrate.pack()

            prespi = tk.Label(dlg, text="Respiration")
            prespi.pack()
            respi = tk.Text(dlg, height=1, width=10)
            respi.insert(tk.END, p[10])
            respi.pack()

            pbloodp = tk.Label(dlg, text="Systolic Blood Pressure")
            pbloodp.pack()
            bloodp = tk.Text(dlg, height=1, width=10)
            bloodp.insert(tk.END, p[11])
            bloodp.pack()
            pbloodpd = tk.Label(dlg, text="Diastolic blood pressure")
            pbloodpd.pack()
            bloodpd = tk.Text(dlg, height=1, width=10)
            bloodpd.insert(tk.END, p[12])
            bloodpd.pack()

            ptemp = tk.Label(dlg, text="Temperature")
            ptemp.pack()
            temp = tk.Text(dlg, height=1, width=10)
            temp.insert(tk.END, "{:.2f}".format(float(p[13])))
            temp.pack()

            def save():
                p[1] = provid.get(1.0, "end-1c")
                p[2] = age.get(1.0, "end-1c")
                p[3] = v.get()
                p[4] = state.get(1.0, "end-1c")
                p[5] = vtchoosen.get()
                p[6] = pweight.get(1.0, "end-1c")
                p[7] = pheight.get(1.0, "end-1c")
                p[8] = bmivalue.get()
                p[9] = heartrate.get(1.0, "end-1c")
                p[10] = respi.get(1.0, "end-1c")
                p[11] = bloodp.get(1.0, "end-1c")
                p[12] = bloodpd.get(1.0, "end-1c")
                p[13] = temp.get(1.0, "end-1c")

                dismiss()


            # create save button
            psave = tk.Button(dlg, text="Save", command=save)
            psave.pack()

            # create cancel button
            pcancel = tk.Button(dlg, text="Cancel", command=dismiss)
            pcancel.pack()


            dlg.protocol("WM_DELETE_WINDOW", dismiss) # intercept close button
            dlg.transient(root)   # dialog window is related to main
            dlg.wait_visibility() # can't grab until window appears, so we wait
            dlg.grab_set()        # ensure all input goes to our window
            dlg.wait_window()     # block until window is destroyed

            # save into the file, the style of p is a list
            with open("patients.csv", "w", newline="") as f:
                w = csv.writer(f, delimiter=",")
                # for headers
                w.writerow(header)
                for p in patients:
                    w.writerow(p)

            break
find_btn = tk.Button(root, text="Find", command=find_patient)
# use pack to show find button
find_btn.pack()


# run the gui window
#root.mainloop()

'''END JIN'S CODE'''

'''THERESA'S GUI SCRIPT'''
'''

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

'''

'''JOHN'S DESCRIPTIVE STATISTICS MODULE AND GUI SCRIPT'''

#root = tk.Tk()
#root.wm_title("Supersquad")
#=tk.Label(root, text="Counts and Statistics")
#w.pack()

tkvar = tk.StringVar(root)
choices = {'Disease at Admission','state','visittype','Comorbidities','provider'}
tkvar.set('state')

a=tk.Label(root, text="Choose a attribute to count:")
a.pack()

popupMenu = tk.OptionMenu(root, tkvar, *choices)
popupMenu.pack()

b=tk.Label(root, text="Choose a grouping and a lab test for Discriptive Statistics:")
b.pack()

def print1(*args):
    T.delete(1.0, tk.END)
    T.insert(tk.END, statistics.counts(tkvar.get()) )   
tkvar.trace('w', print1)

tkvar1 = tk.StringVar(root)
tkvar2 = tk.StringVar(root)
# Dictionary with options
choices1 = {'All',
      'Women Under 65',
      'Women Over 65',
      'Men Under 65',
      'Men Over 65'}
choices2 = {'Triglycerides','HDL','LDL','Total Cholesterol','CRP', 'bmi', 'respiration','systolic blood pressure','diastolic blood pressure','temperature'}
tkvar1.set('All') # set the default option
tkvar2.set('HDL')

popupMenu1 = tk.OptionMenu(root, tkvar1, *choices1,)
popupMenu1.pack()

popupMenu2 = tk.OptionMenu(root, tkvar2, *choices2,)
popupMenu2.pack()

T = tk.Text(root, height=10, width=50)
T.pack()
def holder(*args):
    holder=tkvar1.get()
def print2(*args):
    T.delete(1.0, tk.END)
    T.insert(tk.END, statistics.print_stats(statistics.dfss[tkvar1.get()], tkvar2.get()) )   
tkvar1.trace('w', holder)
tkvar2.trace('w', print2)

tkvar3 = tk.StringVar(root)
choices3 = {'Triglycerides','HDL','LDL','Total Cholesterol','CRP', 'bmi', 'respiration','systolic blood pressure','diastolic blood pressure','temperature'}
tkvar3.set('HDL')

c=tk.Label(root, text="Choose a lab test to graph:")
c.pack()
popupMenu3 = tk.OptionMenu(root, tkvar3, *choices3)
tk.Label(root, text="Choose a Lab Test to Graph")
popupMenu3.pack()


def graph(*args):
    fig=statistics.graphsea(tkvar3.get())
    dlg = tk.Toplevel(root)
    y=tk.Label(dlg, text="Feature")
    y.pack()
    canvas = FigureCanvasTkAgg(fig, master=dlg)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


tkvar3.trace('w', graph)

tk.mainloop()