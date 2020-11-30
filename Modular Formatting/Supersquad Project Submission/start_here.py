#importing necessary python libraries, modules, and packages for patient data generation for this script, module-specific imports are in those files.
import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import pandas as pd
import random

#importing the modules
from patient import patient
from statistics import statistics

'''RUNNING THE PATIENT MODULE'''

# create an empty patients list
patients = []
# create 300 patients by using Patient class in patient module
for i in range(0, 300):
    p = patient.Patient()
    patients.append(p)

# print the whole list, the items in the patients list are all patient.Patient
#print(patients)


with open('patients.csv', 'w', newline='') as file:
    # writer for writing the csv rows in the file
    w = csv.writer(file)
    # use writerow to write the header in csv file
    w.writerow(['id', 'provider', 'age', 'sex', 'state', 'visittype', 'weight', 'height', 'bmi', 'heartrate', 'respiration', 'systolic blood pressure', 'diastolic blood pressure', 'temperature'])
    # write every patient to the csv file
    for p in patients:
        w.writerow([p.id, p.provider, p.age, p.sex, p.state, p.visittype, p.weight, p.height, p.bmi(), p.heart_rate, p.respiration, p.blood_pressure[0], p.blood_pressure[1], "{:.2f}".format(p.temperature)])
file.close()

'''THERESA'S RUNNING THE PATIENT CARDIOVASCULAR DATA MODULE'''

def _makeIDGen(): # setting up Jin's id generator to make a merge point for
    i = 1
    while True:
        yield i
        i += 1

_idGen = _makeIDGen()

_disease_at_admission = ['stroke', 'hernia', 'macular degeneration', 'tuberculosis', 'colitis']

_comorbidities = ['COPD', 'cancer', 'diabetes', 'osteoarthritis', 'depression']


class Adult:               # creating adult class
    def __init__(self):    # costructor of class attributes
        self.id =  next(_idGen)
        self.triglycerides = random.randint(35,200)
        self.HDL = random.randint(20,100)
        self.LDL = random.randint(40,190)
        self.total_cholesterol = random.randint(100,300)
        self.CRP = random.randint(0,12)
        self.disease = random.choice(_disease_at_admission)
        self.comorbidities = random.choice(_comorbidities)

    def __str__(self):  # arranging the attributes into strings
        return f'ID: {self.id}, Triglycerides: {self.triglycerides}, HDL: {self.HDL}, LDL: {self.LDL}, Total Cholesterol: {self.total_cholesterol}, CRP: {self.CRP}, Disease at Admission: {self.disease}, Comorbidity: {self.comorbidities}'
    
    def __repr__(self):
        return str(self)
    
adults = []  # empty list

for i in range(0, 300):  # creating 300 patients in list adults
    a = Adult()
    adults.append(a)    
    
with open('total.csv', 'w', newline='') as file: # opeining a new csv and filing it with 300  patients
    # writer for writing the csv rows in the file
    w = csv.writer(file)
    # use writerow to write the header in csv file
    w.writerow(['id', 'Triglycerides', 'HDL', 'LDL', 'Total Cholesterol', 'CRP', 'Disease at Admission', 'Comobiditiy'])
    # write every patinet to the csv file
    for a in adults:
        w.writerow([a.id, a.triglycerides, a.HDL, a.LDL, a.total_cholesterol, a.CRP, a.disease, a.comorbidities])  
        


p = pd.read_csv("patients.csv")  # making patients.csv into a dataframe

t = pd.read_csv("total.csv")  # making total.csv into a dataframe

merged = p.merge(t, on='id')  # merging the two dataframes into one based on id

merged.to_csv("combo.csv", index = False)  # converting the new dataframe into a csv      

middleman = [] # empty list

with open("combo.csv", 'r') as csvfile:  # opening the new csv
    
    csvreader = csv.reader(csvfile) # making a reader object
    
    for row in csvreader:  # adding each line as an element in middleman
        middleman.append(row)  

middleman.pop(0) #removing the header row

cardio_case=[] # opening an empty list to put the adult patients in


for i in range(300): # all lists in list
    if int(middleman[i][2]) >= 12: # if index 2 of each list is adult
        cardio_case.append(middleman[i]) # add the list to cardio_case


for f in range(len(cardio_case)): # itterate through 300 patients and assign points for certain lab test values
    
    points = 0  # setting point counter to 0
                               
    if int(cardio_case[f][12]) > 150: # if the value at the specified index meets the condition
            points+=1          # a point is added
    
    if cardio_case[f][3] == 'M' and float(cardio_case[f][13]) < 40:   # men and women have diffrent values for high risk 
            points+=1
            
    if cardio_case[f][3] == 'F' and float(cardio_case[f][13]) <50:
            points+=1
   
    if int(cardio_case[f][14]) > 100:
            points+=1
    
    if int(cardio_case[f][15]) > 200:
            points+=1
    
    if int(cardio_case[f][16]) > 2:
            points+=1
    
    
    cardio_case[f].append(str(points)) # adding the point total to patient f


    
for n in range(len(cardio_case)):   # assigning risk category based on index [19] point scores
    
    if float(cardio_case[n][21]) == 0:
             Risk = 'low'
    if float(cardio_case[n][21]) == 1:
             Risk = 'mild'
    if float(cardio_case[n][21]) == 2:
             Risk = 'moderate'
    if float(cardio_case[n][21]) == 3:
             Risk = 'moderate high'
    if float(cardio_case[n][21]) == 4:
             Risk = 'high'
    if float(cardio_case[n][21]) == 5:
             Risk = 'major'
            
    cardio_case[n].append(Risk) # adding risk category to patient n
with open('cardiocases.csv', 'w', newline='') as file: # making the final csv
    # writer for writing the csv rows in the file
    w = csv.writer(file)
    # use writerow to write the header in csv file    
    w.writerow(['id', 'provider', 'age', 'sex', 'state', 'visittype', 'weight', 'height', 'heartrate', 'respiration', 'blood pressure', 'temperature', 'Triglycerides', 'HDL', 'LDL', 'Total Cholesterol', 'CRP', 'Disease at Admission', 'Comobiditiy', 'Risk Score', 'Risk'])
    for c in range(len(cardio_case)): # putting in all patients by index
        w.writerow([cardio_case[c][0], cardio_case[c][1], cardio_case[c][2], cardio_case[c][3], cardio_case[c][4], cardio_case[c][5], cardio_case[c][6], cardio_case[c][7], cardio_case[c][8], cardio_case[c][9], cardio_case[c][10], cardio_case[c][11], cardio_case[c][12], cardio_case[c][13], cardio_case[c][14], cardio_case[c][15], cardio_case[c][16], cardio_case[c][17], cardio_case[c][18], cardio_case[c][19], cardio_case[c][20]])
file.close()



'''JIN'S GUI SCRIPT'''




patients = []
header = []

with open("patients.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    header = next(reader, None)
    for row in reader:
        patients.append(row)

root = tk.Tk()
# adjust the window's size
root.geometry("4000x2400")
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

'''THERESA'S GUI SCRIPT'''


df = pd.read_csv("cardiocases.csv") ## using pandas to make the csv a dataframe

#root = tk.Tk() ## create window
#root.title('Supersquad') ## title of window

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

'''JOHN'S DESCRIPTIVE STATISTICS MODULE AND GUI SCRIPT'''

#root = tk.Tk()
#root.wm_title("Supersquad")
#=tk.Label(root, text="Counts and Statistics")
#w.pack()

tkvar = tk.StringVar(root)
choices = {'Disease at Admission', 'Comobiditiy','state_x','visittype_x','provider_x'}
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
choices2 = {'Triglycerides','HDL','LDL','Total Cholesterol','CRP', 'bmi', 'respiration_y','heartrate_y','systolic blood pressure','diastolic blood pressure'}
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
choices3 = {'Triglycerides','HDL','LDL','Total Cholesterol','CRP', 'bmi', 'respiration','systolic blood pressure','diastolic blood pressure',}
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