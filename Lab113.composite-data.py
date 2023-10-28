print()
print("------------Creating a car inventory program------------------------------")
print()
import csv
import copy
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty",
    "model" : "<empty",
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0,
}
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
myInventoryList = []
with open('Lab113.car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'Column name are: {", ".join(row)}')
            lineCount += 1
        else:
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            myVehicle["vin"] = row[0]  
            myVehicle["make"] = row[1]  
            myVehicle["model"] = row[2]  
            myVehicle["year"] = row[3]  
            myVehicle["range"] = row[4]  
            myVehicle["topSpeed"] = row[5]  
            myVehicle["zeroSixty"] = row[6]  
            myVehicle["mileage"] = row[7]
            myInventoryList.append(myVehicle)
            lineCount += 1
    print(f'Processed {lineCount} lines.')
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key,value))
            print("----------------------")