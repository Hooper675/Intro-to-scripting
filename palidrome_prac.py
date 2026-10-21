user_input = input("write a sentence:")

new_case = user_input.casefold().replace(" ","")

if (new_case == new_case[::-1]) and new_case != "":
    print("It's a palindrom")
else:
    print("It's not a palindrom")