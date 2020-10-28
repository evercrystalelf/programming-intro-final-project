import random
import csv

def _makeIDGen():
    i = 1
    while True:
        yield i
        i += 1

_idGen = _makeIDGen()
_stateset1 = ['Utah', 'Texas', 'Ohio', 'California', 'Idaho', 'Maine', 'Alaska', 'Colorado', 'North Carolina', 'New York']
_visittype = ['primary care', 'specialist', 'hospital inpatient', 'emergency', 'nursing facility']
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

class Patient:
    def __init__(self):
        global _heights
        self.id =  next(_idGen)
        self.provider = random.randint(1, 10)
        self.age = random.randint(1, 100)
        self.sex = random.choice('FM')
        self.state = random.choice(_stateset1)
        self.visittype = random.choice(_visittype)
        self.height = random.choice(list(_heights.keys()))
        self.weight = random.randint(*_heights[self.height])
        if self.age >= 1 and self.age < 6:
            key = "child1"
        elif self.age >= 6 and self.age < 12:
            key = "child2"
        else:
            key = "adult"
        vs = _vital_signs[key]
        self.heart_rate = random.randint(*vs["heartrate"])
        self.respiration = random.randint(*vs["respiration"])
        self.blood_pressure = (random.randint(*vs["blood pressure"][0]), random.randint(*vs["blood pressure"][1]))
        self.temperature = random.uniform(*vs["temperature"])

    def bmi(self):
        return self.weight * 703 / self.height ** 2

    def height_to_ftin(self):
        ft, inch = divmod(self.height, 12)
        return "{}' {}\"".format(ft, inch)

    def __str__(self):
        return f'ID: {self.id}, Provider: {self.provider}, Age: {self.age}, Sex: {self.sex}, State: {self.state}, Visit_type: {self.visittype}, Weight: {self.weight}, Height: {self.height_to_ftin()}, BMI: {self.bmi()}, Heart Rate: {self.heart_rate} bpm, Respiration: {self.respiration} bpm, Blood Pressure: {self.blood_pressure[0]}/{self.blood_pressure[1]} mmHg, Temperature: {self.temperature:.2f}\n'
    
    def __repr__(self):
        return str(self)

# now I'm going to generate the 300 patients


Dataset = [] #opening an empty list
for file in range(301): # because 0 coounts and we want 300
    file = [(Patient())] #making a patient file
    Dataset.append(file)  #filling the empty list with each file as a list 

#print (Dataset) #visual for me 

# now opening a csv file and putting the Dataset in

open('supersquad.csv', 'w', newline='') as file:
    writer.writerows(Dataset)
f.close()

# self.lab = laboratory_tests
# self.disease = disease_at_admission
# self.comorbidities = comorbidities

#laboratory_tests = ['triglycerides', 'HDL', 'LDL', 'total_cholesterol', 'CRP']

#using integers to keep it simple

triglycerides = random.randint(35,200) #mg/dL

HDL = random.randint(20,100) #mg/dL

LDL = random.randint(40,190) #mg/dL

total_cholesterol = random.randint(100,300) #mg/dL

CRP = random.randint(0,12) #mg/L

_disease_at_admission = ['stroke', 'hernia', 'macular degeneration', 'tuberculosis', 'colitis']

_comorbidities = ['COPD', 'cancer', 'diabetes', 'osteoarthritis', 'depression']

self.disease = random.choice(_disease_at_admission)

self.comorbidities = random.chocie(_comorbidities)

# for each patient of the 300 that qualify as "adult" genertate values for their laboratory_tests, 
# _disease_at_admission and _comorbidities and add it to the patient's file This will be a for/if block

cardio_case = []  # opening a new empty list for adults only
    for file in Dataset: # going throught the paitent files
        if Age: >12:  # selecting adults then tacking on laboratory_tests
            cardio_case.append(file + str(triglycerides, HDL, LDL, total_cholesterol, CRP, self.disease, self.comorbidities)
  
        
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
