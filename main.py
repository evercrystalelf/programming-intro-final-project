from patient import patient

import random
import csv

patients = []
for i in range(0, 300):
    p = patient.Patient()
    patients.append(p)
#print(patients)

open('patients.csv', 'w', newline='') as file:
   writer.writerows(patients)
f.close()    

#laboratory_tests = ['triglycerides', 'HDL', 'LDL', 'total_cholesterol', 'CRP']

triglycerides = random.randint(35,200) #mg/dL

HDL = random.randint(20,100) #mg/dL

LDL = random.randint(40,190) #mg/dL

total_cholesterol = random.randint(100,300) #mg/dL

CRP = random.randint(0,12) #mg/L

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

# for each patient of the 300 that qualify as "adult" genertate values for their laboratory_tests, 
# _disease_at_admission and _comorbidities and add it to the patient's file This will be a for/if block

cardio_case = []  # opening a new empty list for adults only

cardio_case.append(list(filter(lambda x: x.age >= 12, patients))) #get all the adults into a list

#tacking on laboratory_test values

for file in cardio_case:
    cardio_case.append(triglycerides{self.triglycerides}, HDL{self.HDL}, LDL{self.LDL}, total_cholesterol{self.total_cholesterol}, CRP{self.CRP}, disease_at_admission{self.disease_at_admission}, comorbidities{self.comobidities})
  
        
# now to use the laboratory_test values to asses the risk value for cardivascular disease.
# This will be done by assigning points, once the points are added the risk score which we define will be retuned
# a point will be given for each value meeting the following:
# total_cholesterol > 200
# LDL > 100
# HDL for men < 40, for women < 50
# triglycerides > 150
# CRP > 2

def risk_score ():
    points = 0   #setting itteration value to 0 for addition
    
    for f in cardio_case:                           
                               
    
        if triglyceride > 150: # if the value meets the condition
            points+=1          # a point is added
    
        if sex = M and HDL < 40:
            points+=1
            else:
                if sex = F and HDL <50:
                    points+=1
   
                               
        if LDL > 100:
            points+=1
    
        if total_cholesterol > 200:
            points+=1
    
        if CRP > 2:
            points+=1
    
    risk_score = points # the total points
    
    cardio_case = f.cardio_case.append(risk_score) # adding the point total to the adult patients

def Risk ():      # assigning each total point possibliity to a risk estimation
    for item in cardio_case:
        if points = 0:
            Risk = low
        if points = 1:
            Risk = mild
        if points = 2:
            Risk = moderate
        if points = 3:
            Risk = moderate high
        if points = 4:
            Risk = high
        if points = 5:
            Risk = major
    cardio_case = item.cardio_case.append(Risk)

# now opening a csv file and putting the adult cardio cases in

open('cardio_case.csv', 'w', newline='') as file:
   writer.writerows(cardio_case)
f.close()    
