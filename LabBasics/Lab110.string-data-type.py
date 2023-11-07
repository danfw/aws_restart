print("------------Exercise 1 | String--------------")
print()
myString= "This is a string."
print(myString)
print(type(myString))
print(str(myString) + " is of the data type " + str(type(myString)))
print()
print("------------Exercise 2 | Working string Concatenation--------------")
print()
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
print()
print("------------Exercise 3 | Working Input Strings--------------")
print()
name = input("What is your name?; please type it: ")
print(name)
print()
print("------------Exercise 4 | Formatting output strings--------------")
print()
color = input("What is your favorite color?: ")
animal = input("What is your favorite animal?: ")
print("{}, I am pretty sure that you like to see a {} {}!".format(name,color,animal))