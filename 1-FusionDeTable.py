import csv

with open ('Contact2.csv') as Contact2 :
    data = list(csv.reader(Contact2))

with open ('contact.csv') as contact :
    data1 = list(csv.reader(contact))

data3 = data1 + data
print(data3)