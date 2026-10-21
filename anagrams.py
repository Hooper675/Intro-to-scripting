user_input = input("enter a text:")
user_input1 = input("enter a second text:")

first = sorted(user_input.casefold())
second = sorted(user_input1.casefold())

if first == second and len(first) >0:
    print("Anagrams")
else:
    print("Not anagrams")