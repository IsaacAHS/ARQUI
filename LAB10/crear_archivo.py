import csv
import random

data= [["paciente", "edad", "diagnostico"]]
for i in range(1,11):
    data.append([i,random.randint(20,60), random.randint(0,1)])
with open('pacientes.csv', 'w') as file:
    for row in data:
        file.write(','.join(map(str,row))+'\n')