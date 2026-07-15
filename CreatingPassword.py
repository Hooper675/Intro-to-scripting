# FIXME (1): Finish reading another word and an integer into variables.
# Output all the values on a single line
favorite_color = input("Enter favorite color:\n")
pet_name = input("Enter your pet name:\n")
age_pet = input("Enter your pet's age:\n")

print(f"You entered: {favorite_color} {pet_name} {age_pet}")

# FIXME (2): Output two password options
password1 = "_".join([favorite_color, pet_name])

password2 = "".join([age_pet,favorite_color,age_pet])

print(f"\nFirst password: {password1}")
print(f"Second password: {password2}")

# FIXME (3): Output the length of the two password options
num_char_password1 = len(password1)
num_char_password2 = len(password2)
print(f"\nNumber of characters in {password1}: {num_char_password1}")
print(f"Number of characters in {password2}: {num_char_password2}")