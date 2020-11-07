import csv
import random

middleman = [] # opening any empty list to put in all the adult patients

with open("patients.csv", 'r') as csvfile: 
    
    csvreader = csv.reader(csvfile) # making a reader object
    
    for row in csvreader:  # adding each line as an element in middleman
        middleman.append(row)  
        
middleman.pop(0) #removing the header row

cardio_case=[] #opening an empty list to put the adult patients in


for i in range(300): # all lists in list
    if int(middleman[i][2]) >= 12: # if index 2 of each list is adult
        cardio_case.append(middleman[i]) # add the list to cardio_case
        
_disease_at_admission = ['stroke', 'hernia', 'macular degeneration', 'tuberculosis', 'colitis']

_comorbidities = ['COPD', 'cancer', 'diabetes', 'osteoarthritis', 'depression']

class Adult:
    def __init__(self):
        self.triglycerides = random.randint(35,200)
        self.HDL = random.randint(20,100)
        self.LDL = random.randint(40,190)
        self.total_cholesterol = random.randint(100,300)
        self.CRP = random.randint(0,12)
        self.disease = random.choice(_disease_at_admission)
        self.comorbidities = random.choice(_comorbidities)

    def __str__(self):
        return f'{self.triglycerides}, {self.HDL}, {self.LDL}, {self.total_cholesterol}, {self.CRP}, {self.disease}, {self.comorbidities}'
    
    def __repr__(self):
        return str(self)
    
for i in range(len(cardio_case)):
    case = Adult()
    cardio_case[i].append(case)    

with open('transform.csv', 'w', newline='') as file:
    w = csv.writer(file)
    w.writerow(cardio_case)

cardio_casecont = [] # opening an intermediate list

with open("transform.csv", 'r') as csvfile: 
    csvreader = csv.reader(csvfile) # making a reader object
    for row in csvreader:  # adding each line as an element in cardio_casecont
        cardio_casecont.append(row)  

print(len(cardio_casecont))
