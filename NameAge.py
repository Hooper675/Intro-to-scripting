# The user will enter their name and age.
# The inputs will be assigned to variables user_name and user_age
user_name = input("What is your name? ")
user_age = int(input("How old are you?"))

# Calculate the year based on the assumption 2020
user_birth_year = 2026 - user_age

#Output the feedback with the user's name and calculated birth year
print(f"Hello {user_name}! You were born in {user_birth_year}")
