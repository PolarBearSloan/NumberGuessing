#Tutorial followed with TechWithTim YouTube 7Jan2022#

import random

#User input to select range of numbers#
topNumber = input("Type a number to stop at: ")

if topNumber.isdigit():
    topNumber = int(topNumber)

    if topNumber <= 0:
        print("Please type a number greater than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

#Select random number from (start,stop)#
randomNumber = random.randint(1,topNumber)

#Guess counter
guesses = 0

while True:
    guesses += 1
    guess = input("Guess the number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number.")
        continue
    if guess == randomNumber:
        print("You got it!!!")
        break
    elif guess > randomNumber:
        print("You're above it.")
    else:
        print("You're below it.")

print("It took you" , guesses, "guesses to get it.")