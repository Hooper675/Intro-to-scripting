# import random module
#Input your name here
#Output Welcome to the high or low game, name
# input Enter a number for lower bound
# input Enter a number for upper bound
# while lower bound >= upper bound:
        #output error.
        # input lower bound
        #input upper bound
# set random number = generate a random number between lower and upper bound
# set number_guess to 0

    # while random number is not equal to the number of guess
              # Great, now guess a number between lower bound number and upper bound number
              # input number_guess
              # while number_guess is less than lower bound or greater than upperbound
                         # output "Invalid guess. Enter a number between lower and upper bound
                         #input number_guess
              # if  number_guess is lower than random number
                       # output Nope too low
              # else if number_guess is higher than random number
                                # output nope too high.
                       # else
                             # output you got it!
import random

name = input("Enter your name: ")
print(f"Welcome to the high or low game, {name}!")

lower_band = int(input("Enter the lower band of the game: "))
upper_band = int(input("Enter the upper band of the game: "))
while lower_band >= upper_band:
    print(" Out of Band. Please choose another band or try again.")
    lower_band = int(input("Enter the lower band of the game: "))
    upper_band = int(input("Enter the upper band of the game: "))

random_number = random.randint(lower_band, upper_band)
number_guess = 0
while random_number != number_guess:
    print(f"Great, now guess a number between {lower_band} and {upper_band}")
    number_guess = int(input("Enter your guess: "))

    while number_guess < lower_band or number_guess > upper_band:
        print(f"Invalid guess. Enter a number between {lower_band} and {upper_band}")
        number_guess = int(input("Enter your guess: "))
    if number_guess < random_number:
        print("Nope! too low")
    elif number_guess > random_number:
        print("Nope! too high")
    else:
        print("You got it!")

