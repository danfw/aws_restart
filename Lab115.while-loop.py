#Random is the avality to get a random value
import random
print()
print("------------1 | Working with a while loop------------------------------")
print()
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#Right here a Get a Integer Random number
number = random.randint(1,10)

#Condition start with false, so when while starts go directly to loop until  user choose the right number
isGuestRight = False

while isGuestRight != True:
    guess = input("Guess a number betwwen 1 and 10 (type it): ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You Win!".format(guess))
        isGuestRight = True
    else:
        print("You guessd {}. Sorry, that isn't it. Try again.".format(guess))
    