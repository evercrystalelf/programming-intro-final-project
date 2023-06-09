import random
import csv
import pandas as pd

def patient_cardiovascular():
    def _makeIDGen():
        i = 1
        while True:
            yield i
            i += 1

    _idGen = _makeIDGen()

    class Adult:
        def __init__(self):
            self.id =  next(_idGen)
            self.triglycerides = random.randint(35,200)
            self.HDL = random.randint(20,100)
            self.LDL = random.randint(40,190)
            self.total_cholesterol = random.randint(100,300)
            self.CRP = random.randint(0,12)
            self.disease = random.choice(_disease_at_admission)
            self.comorbidities = random.choice(_comorbidities)

        def __str__(self):
            return f'ID: {self.id}, Triglycerides: {self.triglycerides}, HDL: {self.HDL}, LDL: {self.LDL}, Total Cholesterol: {self.total_cholesterol}, CRP: {self.CRP}, Disease at Admission: {self.disease}, Comorbidity: {self.comorbidities}'
        
        def __repr__(self):
            return str(self)
        
    adults = []

    for i in range(0, 300):
        a = Adult()
        adults.append(a)    
        
    with open('total.csv', 'w', newline='') as file:
        # writer for writing the csv rows in the file
        w = csv.writer(file)
        # use writerow to write the header in csv file
        w.writerow(['id', 'Triglycerides', 'HDL', 'LDL', 'Total Cholesterol', 'CRP', 'Disease at Admission', 'Comobiditiy'])
        # write every patinet to the csv file
        for a in adults:
            w.writerow([a.id, a.triglycerides, a.HDL, a.LDL, a.total_cholesterol, a.CRP, a.disease, a.comorbidities])  
            
    import pandas as pd

    p = pd.read_csv("patients.csv")

    t = pd.read_csv("total.csv")

    merged = p.merge(t, on='id')

    merged.to_csv("combo.csv", index = False)        

    middleman = [] 

    with open("combo.csv", 'r') as csvfile: 
        
        csvreader = csv.reader(csvfile) # making a reader object
        
        for row in csvreader:  # adding each line as an element in middleman
            middleman.append(row)  

    middleman.pop(0) #removing the header row

    cardio_case=[] #opening an empty list to put the adult patients in


    for i in range(300): # all lists in list
        if int(middleman[i][2]) >= 12: # if index 2 of each list is adult
            cardio_case.append(middleman[i]) # add the list to cardio_case



    for f in range(len(cardio_case)): 
        
        points = 0
                                
        if int(cardio_case[f][12]) > 150: # if the value meets the condition
                points+=1          # a point is added
        
        if cardio_case[f][3] == 'M' and int(cardio_case[f][13]) < 40:
                points+=1
                
        if cardio_case[f][3] == 'F' and int(cardio_case[f][13]) <50:
                points+=1
    
        if int(cardio_case[f][14]) > 100:
                points+=1
        
        if int(cardio_case[f][15]) > 200:
                points+=1
        
        if int(cardio_case[f][16]) > 2:
                points+=1
        
        
        cardio_case[f].append(str(points)) # adding the point total to the adult patients


        
    for n in range(len(cardio_case)):
        
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
                
        cardio_case[n].append(Risk)

    with open('cardiocases.csv', 'w', newline='') as file:
        # writer for writing the csv rows in the file
        w = csv.writer(file)
        # use writerow to write the header in csv file    
        w.writerow(['id', 'provider', 'age', 'sex', 'state', 'visittype', 'weight', 'height', 'heartrate', 'respiration', 'blood pressure', 'temperature', 'Triglycerides', 'HDL', 'LDL', 'Total Cholesterol', 'CRP', 'Disease at Admission', 'Comobiditiy', 'Risk Score', 'Risk'])
        for c in range(len(cardio_case)):
            w.writerow([cardio_case[c][0], cardio_case[c][1], cardio_case[c][2], cardio_case[c][3], cardio_case[c][4], cardio_case[c][5], cardio_case[c][6], cardio_case[c][7], cardio_case[c][8], cardio_case[c][9], cardio_case[c][10], cardio_case[c][11], cardio_case[c][12], cardio_case[c][13], cardio_case[c][14], cardio_case[c][15], cardio_case[c][16], cardio_case[c][17], cardio_case[c][18], cardio_case[c][19], cardio_case[c][20]])
        