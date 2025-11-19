import csv

limit = int(input("Enter the limit : "))

myDict = []

for i in range(limit):
    print("Enter the details of student number ",i+1, " : ")
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    mark = int(input("Enter mark : "))
    myDict.append({"name":name, "age":age, "mark":mark})

with open("new.csv", "w+", newline = "") as newcsv:
    writer = csv.writer(newcsv)

    writer.writerow(['Name', 'Age', 'Mark'])

    for i in range(limit):
        writer.writerow([myDict[i]["name"], myDict[i]["age"], myDict[i]["mark"]])

    newcsv.flush()
    newcsv.seek(0)

    reader = csv.reader(newcsv)

    next(reader)

    for row in reader:
        print(row)