from patient import patient

import random
import csv

patients = []
for i in range(0, 300):
    p = patient.Patient()
    patients.append(p)
#print(patients)

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
        self.totalcholesterol = random.randint(100,300)
        self.CRP = random.randint(0,12)
        self.disease = random.choice(_disease_at_admission)
        self.comorbidities = random.choice(_comorbidities)

# for each patient of the 300 that qualify as "adult" genertate values for their laboratory_tests, 
# _disease_at_admission and _comorbidities and add it to the patient's file This will be a for/if block

cardio_case = []  # opening a new empty list for adults only
    for file in patients: # going throught the paitent files
        if Age: >12:  # selecting adults then tacking on laboratory_tests
            cardio_case.append(file)
    for file in cardio_case:
        cardio_case.append(
  
        
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
                               
    
        if triglyceride > 150:
            points+=1
    
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
    
    risk_score = points
    
    cardio_case = f.cardio_case.append(points) # adding the point total to the adult patients

def Risk ():
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
