import random

# Pat = dict()
# for i in range(301):
# P = Patient
# Pat[patientID] = P

# providerID = random.randint(1, 10)
# age = random.randint(1, 100)
# Sex = random.choice('FM')
# state = 
# visit_type = random.choice(['VT1', 'VT2', 'VT3', 'VT4', 'VT5'])
# height = 
# weight = 
# BMI = 
# vital_signs = ['temperature', 'pulse', 'respiration', 'blood pressure']

# temperature = (random.uniform(36.0, 37.5), %.2f)

# if age <= 11:
#     pulse = random.randint(70, 120)
#     print(pulse, 'bpm')
# else:
#     pulse = random.randint(60, 100)
#     print(pulse, 'bpm')

# if age <= 5:
#     respiration = random.randint(20, 30)
#     print(respiration, 'bpm')
# elif age <= 11:
#     respiration = random.randint(12, 20)
#     print(respiration, 'bpm')
# else:
#     respiration = random.randint(12, 18)
#     print(respiration, 'bpm')
# if age <= 11:
#     systolic = random.randint(90, 110)
#     diastolic = random.randint(55, 75)
#     blood pressure = (systolic, diastolic, 'mmHg')



patientID = 0
class Patient:
    def __init__(self):
        global patientID 
        patientID += 1
        self.ID =  patientID
        # self.provider = providerID
        self.age = random.randint(1, 100)
        # self.sex = Sex
        # self.state = state
        # self.visit = visit_type
        # self.height = height
        # self.weight = weight
        # self.BMI = BMI
        # self.vital_sign = vital_signs
        # self.lab = laboratory_tests
        # self.disease = disease_at_admission
        # self.comorbidities = comorbidities

    def __str__(self):
        return "ID: {}, Age: {}".format(self.ID, self.age)
    

    def __repr__(self):
        return str(self)

