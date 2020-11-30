import tkinter as tk
import csv
from tkinter import *
from tkinter import ttk


patients = []
header = []

with open("patients.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    header = next(reader, None)
    for row in reader:
        patients.append(row)

# import Tkinter as tk

# after importing tk, use Tk class creating window, and save in root variable
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
root.mainloop()
