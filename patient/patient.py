import random

def _makeIDGen():
    i = 1
    while True:
        yield i
        i += 1

_idGen = _makeIDGen()
_stateset1 = ['Utah', 'Texas', 'Ohio', 'California', 'Idaho', 'Maine', 'Alaska', 'Colorado', 'North Carolina', 'New York']
_visittype = ['VT1', 'VT2', 'VT3', 'VT4', 'VT5']
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

