# import random for generating random data
import random
import csv

# make a patient id generator which is protected
def _makeIDGen():
    i = 1
    while True:
        yield i
        i += 1
# create a generator, and can use the same instance for every new Patient 
_idGen = _makeIDGen()
# a protected list of states
_stateset1 = ['Utah', 'Texas', 'Ohio', 'California', 'Idaho', 'Maine', 'Alaska', 'Colorado', 'North Carolina', 'New York']
# a protected list of visittypes
_visittype = ['primary care', 'specialist', 'hospital inpatient', 'emergency', 'nursing facility']
# a protected dictionary of heights, key is height in inches while the value is a tuple of weight ranges (min, max)
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
# a protected dictionary of vitalsigns, keys are different groups based on age range, the value is another dictionary.
# In the sub dictionaries, the keys are different vitalsigns, and the values are tuple with range for that vital sign.
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
# class named Patient, and use __init__ to initiate attributes under the class, using random values
class Patient:
    def __init__(self):
        # use global in case if there's assigned height, then BMI vlaue can change based on the assigned value
        global _heights 

        # use next to iterate generator of yield, ID starts at 1
        self.id =  next(_idGen) 

        # generate random provider ID include start and end
        self.provider = random.randint(1, 10) 
        
        # generate random age include start and end
        self.age = random.randint(1, 100)  
        
        # randomly choose F or M
        self.sex = random.choice('FM')  
        
        # randomly choose from stateset1
        self.state = random.choice(_stateset1)   
        
        # randomly choose from visittype
        self.visittype = random.choice(_visittype)  
        
        # randomly choose from the keys in height dictionary, those keys were put in a list 
        self.height = random.choice(list(_heights.keys())) 
        
        # get the value from chosen key name(use self.height), and use * to unpack the value in tuple. Finally use randint to generate a random weight
        self.weight = random.randint(*_heights[self.height])  

        # to know which age is in which key in vitalsigns
        if self.age >= 1 and self.age < 6:   
            key = "child1"
        elif self.age >= 6 and self.age < 12:
            key = "child2"
        else:
            key = "adult"

        # vs is the vitalsigns dictionary based on which key was chosen 
        vs = _vital_signs[key]
        
        # key in vs dictionary, and use * to unpack the value in the tuple, finally use randint to generate data
        self.heart_rate = random.randint(*vs["heartrate"])   
        self.respiration = random.randint(*vs["respiration"])
        
        # index 0 for the first tuple, index 1 for the second tuple
        self.blood_pressure = (random.randint(*vs["blood pressure"][0]), random.randint(*vs["blood pressure"][1]))
        self.temperature = random.uniform(*vs["temperature"])

    # bmi definition to calculate bmi for USA units 
    def bmi(self):
        return self.weight * 703 / self.height ** 2

    # definition to convert inches to ft and inch
    def height_to_ftin(self):
        ft, inch = divmod(self.height, 12)
        return "{}' {}\"".format(ft, inch)

    # use def __str__ for a string representation of this object
    def __str__(self):
        return f'ID: {self.id}, Provider: {self.provider}, Age: {self.age}, Sex: {self.sex}, State: {self.state}, Visit_type: {self.visittype}, Weight: {self.weight}, Height: {self.height_to_ftin()}, BMI: {self.bmi()}, Heart Rate: {self.heart_rate} bpm, Respiration: {self.respiration} bpm, Blood Pressure: {self.blood_pressure[0]}/{self.blood_pressure[1]} mmHg, Temperature: {self.temperature:.2f}\n'

    # use def __repr__ and str(self) present the items in the patients list as string
    def __repr__(self):
        return str(self)

# create an empty patients list
patients = []
# create 300 patients by using Patinet class in patient module
for i in range(0, 300):
    p = Patient()
    patients.append(p)

# print the whole list, the items in the patients list are all patient.Patient
print(patients)


with open('patients.csv', 'w', newline='') as file:
    # writer for writing the csv rows in the file
    w = csv.writer(file)
    # use writerow to write the header in csv file
    w.writerow(['id', 'provider', 'age', 'sex', 'state', 'visittype', 'weight', 'height', 'bmi', 'heartrate', 'respiration', 'systolic blood pressure', 'diastolic blood pressure', 'temperature'])
    # write every patient to the csv file
    for p in patients:
        w.writerow([p.id, p.provider, p.age, p.sex, p.state, p.visittype, p.weight, p.height, p.bmi(), p.heart_rate, p.respiration, p.blood_pressure[0], p.blood_pressure[1], "{:.2f}".format(p.temperature)])
        
