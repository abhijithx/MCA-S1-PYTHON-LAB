import csv

f=open("data.csv","r")
r = csv.reader(f)
for row in r:
        print(row)
