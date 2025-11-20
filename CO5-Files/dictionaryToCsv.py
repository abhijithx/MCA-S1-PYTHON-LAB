import csv

data = [
    {"Name": "Alice", "Age": 23, "City": "London"},
    {"Name": "Bob", "Age": 30, "City": "New York"}
   
]


with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    
    writer.writerow(["Name", "Age", "City"])
    
    for row in data:
        writer.writerow([row["Name"], row["Age"], row["City"]])


with open("output.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
