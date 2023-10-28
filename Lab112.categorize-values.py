print()
print("------------Exercise 1 | Creating a mixed-type list------------------------------")
print()
myMixedTupeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTupeList:
    print("{} is of the data type {}".format(item,type(item)))