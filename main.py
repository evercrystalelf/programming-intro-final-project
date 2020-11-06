import random
import csv
# import patient module
from patient import patient

# create an empty patients list
patients = []
# create 300 patients by using Patinet class in patient module
for i in range(0, 300):
    p = patient.Patient()
    patients.append(p)

# print the whole list, the items in the patients list are all patient.Patient
print(patients)


with open('patients.csv', 'w', newline='') as file:
    # writer for writing the csv rows in the file
    w = csv.writer(file)
    # use writerow to write the header in csv file
    w.writerow(['id', 'provider', 'age', 'sex', 'state', 'visittype', 'weight', 'height', 'heartrate', 'respiration', 'blood pressure', 'temperature'])
    # write every patinet to the csv file
    for p in patients:
        w.writerow([p.id, p.provider, p.age, p.sex, p.state, p.visittype, p.weight, p.height, p.heart_rate, p.respiration, p.blood_pressure, p.temperature])
        
#laboratory_tests = ['triglycerides', 'HDL', 'LDL', 'total_cholesterol', 'CRP']

#triglycerides = random.randint(35,200) #mg/dL

#HDL = random.randint(20,100) #mg/dL

#LDL = random.randint(40,190) #mg/dL

#total_cholesterol = random.randint(100,300) #mg/dL

#CRP = random.randint(0,12) #mg/L

_disease_at_admission = ['stroke', 'hernia', 'macular degeneration', 'tuberculosis', 'colitis']

_comorbidities = ['COPD', 'cancer', 'diabetes', 'osteoarthritis', 'depression']

class Adult:   # creating a class called Adult
    def __init__(self):   # constructing the objet
        self.triglycerides = random.randint(35,200) #mg/dL
        self.HDL = random.randint(20,100) #mg/dL
        self.LDL = random.randint(40,190) #mg/dL
        self.total_cholesterol = random.randint(100,300) #mg/dL
        self.CRP = random.randint(0,12) # mg/L
        self.disease = random.choice(_disease_at_admission) 
        self.comorbidities = random.choice(_comorbidities)
     
    def __str__(self):
        return f'Triglycerides: {self.triglycerides}, HDL: {self.HDL}, LDL: {self.LDL}, Total Cholesterol: {self.total_cholesterol}, CRP: {self.CRP}, Disease at Admission: {self.disease}, Comorbidities: {self.comorbidities})'

    def __repr__(self):
        return str(self)
    
        # for each patient of the 300 that qualify as "adult" genertate values for their laboratory_tests, 
        # _disease_at_admission and _comorbidities and add it to the patient's file

middleman = [] # opening any empty list to put in all the adult patients

with open("patients.csv", 'r') as csvfile: # opening paitents file 
    csvreader = csv.reader(csvfile) # making a reader object
    for row in csvreader:  # adding each line as an element in middleman
        middleman.append(row)  
        
middleman.pop(0) #removing the header row

cardio_case=[] #opening an empty list to put the adult patients in


for i in range(300): # all lists in list
    if int(middleman[i][2]) >= 12: # if index 2 of each list is adult
        cardio_case.append(middleman[i]) # add the list to cardio_case
        
for i in range(len(cardio_case)):
    case = Adult()
    cardio_case[i].append(case)            
        
                
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

        if string.index (M,34,36) and HDL < 40:
            points+=1

        if string.index (F,34,36) and HDL <50:
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
        if points == 0:
            Risk = 'low'
        if points == 1:
            Risk = 'mild'
        if points == 2:
            Risk = 'moderate'
        if points == 3:
            Risk = 'moderate high'
        if points == 4:
            Risk = 'high'
        if points == 5:
            Risk = 'major'
    cardio_case = item.cardio_case.append(Risk)

# now opening a csv file and putting the adult cardio cases in

with open('cardio_case.csv', 'w', newline='') as file:
    w = csv.writer(file)
    writer.writerows(cardio_case)
    w.writerow(['id', 'provider', 'age', 'sex', 'state', 'visittype', 'weight', 'height', 'heartrate', 'respiration', 'blood pressure', 'temperature','triglycerides', 'HDL', 'LDL', 'total cholesterol', 'CRP', 'disease at admission', 'comorbities', 'risk score', 'overall risk'])
    for f in cardio_case:
       w.writerow([f.id, f.provider, f.age, f.sex, f.state, f.visittype, f.weight, f.height, f.heart_rate, f.respiration, f.blood_pressure, f.temperature, f.triglycerides, f.HDL, f.LDL, f.total_cholesterol, f.CRP, f._disease_at_admission, f._comorbities, f.risk_score, f.Risk])
