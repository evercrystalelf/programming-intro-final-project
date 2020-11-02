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
# demonstrate an example to filter for a specific requirement
print(list(filter(lambda x: x.age >= 12, patients)))