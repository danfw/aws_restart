print()
print("---------------------------------------")
print()
myDict = {}
myDict["one"] = 1
myDict["two"] = 2
myDict[3] = "three"
myDict["four"] = 4.4
print()
print("---Direct item------------------------------------")
print()
print(myDict[3])
print()
print("---all items------------------------------------")
print()
for key, value in myDict.items():
    print(key,value)

print()
print("---------------------------------------")
print()