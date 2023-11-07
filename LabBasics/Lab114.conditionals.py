print()
print("------------1 | Working with the if statement------------------------------")
print()
userReply = input("Do you need to ship a package? -- Enter 1(for Yes) or 2(for No): ")
if userReply == "1":
    print("We can help you ship that package!")
    userServices = input("Would you like to buy (1)stamps, buy an (2)envelope, or make a (3)copy; please type the correspondent number: ")
    if userServices == "1":
        print("We have many stamp designs to choose from. Please call +523316051236 to get more information")
    elif userServices == "2":
        print("We have many envelope sizes to choose from. Please call +523316051236 to get more information")
    elif userServices == "3":
        copies = input("How many copies would you like? (Enter a number) ")
        print("Here are {} copies.  Please call +523316051236 to get your copies".format(copies))
    else:
        print("Thank you, please come again.")
else:
    print("Please come back when you need to ship a package. Thank you.")
print()
print("--------------------------------------------------------------------------")
print()

