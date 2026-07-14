# Here you can practice and get help on the exercise to find the smallest of 3 integers.
# Add code to do what the comments describe.

# For each of three numbers, prompt for it to be input and assign a variable to the integer value of what was input.

num_one = int(input("Enter an integer:"))
num_two = int(input("Enter a second integer:"))
num_three = int(input("Enter a third integer:"))

# Add conditional logic to calculate the smallest number. Your code should work even if two or all three of the numbers are equal.

# Print the smallest number.
if (num_one <= num_two) and (num_one <= num_three):
    print(f"{num_one} is the smallest number.")
elif (num_two <= num_one) and (num_two <= num_three):
    print(f"{num_two} is the smallest number.")
else:
    print(f"{num_three} is the smallest number.")