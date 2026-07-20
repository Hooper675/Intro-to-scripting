#calculates the number of times the sum of the randomly rolled dice equals each possible value from 2 to 12.
#repeatedly asks the user for the number of times to roll the dice,
# quitting only when the user-entered number is less than 1.
# Hint: Use a while loop that will execute as long as num_rolls is greater than or equal to 1.
#prints a histogram in which the total number of times the dice rolls equals each possible value
# and is displayed by printing a character, such as *,
# that number of times. Ex:
#Dice roll histogram:
# 2s:  **
# 3s:  ****
# 4s:  ***
# 5s:  ********
# 6s:  *************
# 7s:  *****************
# 8s:  *************
# 9s:  *********
# 10s: **********
# 11s: *****
# 12s: **

import random

num_twos = ""
num_threes = ""
num_fours = ""
num_fives = ""
num_sixes = ""
num_sevens = ""
num_eights = ""
num_nines = ""
num_tens = ""
num_elevens = ""
num_twelves = ""

num_rolls = int(input("Enter number of rolls:\n "))
# repeatedly asks the user for the number of times to roll the dice,
# quitting only when the user-entered number is less than 1.
while num_rolls >= 1:
    for num in range(num_rolls):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        roll_total = dice1 + dice2
# calculates the number of times the sum of the randomly
# rolled dice equals each possible value from 2 to 12
        if roll_total == 2:
            num_twos += "*"
        if roll_total == 3:
            num_threes += "*"
        if roll_total == 4:
            num_fours += "*"
        if roll_total == 5:
            num_fives += "*"
        if roll_total == 6:
            num_sixes += "*"
        if roll_total == 7:
            num_sevens += "*"
        if roll_total == 8:
            num_eights += "*"
        if roll_total == 9:
            num_nines += "*"
        if roll_total == 10:
            num_tens += "*"
        if roll_total == 11:
            num_elevens += "*"
        if roll_total == 12:
            num_twelves += "*"
        print(f"Roll {num} is roll_total: {roll_total} {dice1} + {dice2}")
    print(f"Dice roll statistics:")
    print(f"2s: {num_twos}")
    print(f"3s: {num_threes}")
    print(f"4s: {num_fours}")
    print(f"5s: {num_fives}")
    print(f"6s: {num_sixes}")
    print(f"7s: {num_sevens}")
    print(f"8s: {num_eights}")
    print(f"9s: {num_nines}")
    print(f"10s: {num_tens}")
    print(f"11s: {num_elevens}")
    print(f"12s: {num_twelves}")
    num_rolls = int(input("Enter number of rolls:\n "))

else:
    print("Invalid number of rolls. Try again.")




