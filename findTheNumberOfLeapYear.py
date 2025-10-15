# print("Hello, world!")
import datetime
startYear = datetime.datetime.now().year
endYear = int(input("enter the ending year :"))
print("Leap years :")
while (startYear <= endYear):
    if(startYear % 4 == 0 and  startYear %100 != 0 ) or (startYear % 400 == 0):
        print(startYear)
    startYear+=1    
              
     
