import random ## importing modules
import csv
import pandas as pd

def _makeIDGen(): # setting up Jin's id generator to make a merge point for
    i = 1
    while True:
        yield i
        i += 1

_idGen = _makeIDGen()

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
    
    if cardio_case[f][3] == 'M' and int(cardio_case[f][13]) < 40:   # men and women have diffrent values for high risk 
            points+=1
            
    if cardio_case[f][3] == 'F' and int(cardio_case[f][13]) <50:
            points+=1
   
    if int(cardio_case[f][14]) > 100:
            points+=1
    
    if int(cardio_case[f][15]) > 200:
            points+=1
    
    if int(cardio_case[f][16]) > 2:
            points+=1
    
    
    cardio_case[f].append(str(points)) # adding the point total to patient f


    
for n in range(len(cardio_case)):   # assigning risk category based on index [19] point scores
    
    if int(cardio_case[n][19]) == 0:
             Risk = 'low'
    if int(cardio_case[n][19]) == 1:
             Risk = 'mild'
    if int(cardio_case[n][19]) == 2:
             Risk = 'moderate'
    if int(cardio_case[n][19]) == 3:
             Risk = 'moderate high'
    if int(cardio_case[n][19]) == 4:
             Risk = 'high'
    if int(cardio_case[n][19]) == 5:
             Risk = 'major'
            
    cardio_case[n].append(Risk) # adding risk category to patient n

with open('cardiocases.csv', 'w', newline='') as file: # making the final csv
    # writer for writing the csv rows in the file
    w = csv.writer(file)
    # use writerow to write the header in csv file    
    w.writerow(['id', 'provider', 'age', 'sex', 'state', 'visittype', 'weight', 'height', 'heartrate', 'respiration', 'blood pressure', 'temperature', 'Triglycerides', 'HDL', 'LDL', 'Total Cholesterol', 'CRP', 'Disease at Admission', 'Comobiditiy', 'Risk Score', 'Risk'])
    for c in range(len(cardio_case)): # putting in all patients by index
        w.writerow([cardio_case[c][0], cardio_case[c][1], cardio_case[c][2], cardio_case[c][3], cardio_case[c][4], cardio_case[c][5], cardio_case[c][6], cardio_case[c][7], cardio_case[c][8], cardio_case[c][9], cardio_case[c][10], cardio_case[c][11], cardio_case[c][12], cardio_case[c][13], cardio_case[c][14], cardio_case[c][15], cardio_case[c][16], cardio_case[c][17], cardio_case[c][18], cardio_case[c][19], cardio_case[c][20]])
      
