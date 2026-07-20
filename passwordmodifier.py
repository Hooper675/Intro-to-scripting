# input created password
# set a place holder in password
# for each  letter in the user input words
# if the letter is i:
# append 1 to password
# else if a:
# append @ to password
# else if  m then:
# append M to password
# else if  B :
# append 8 to password
# else if  s:
# append $ to password
# else append the rest to password
# append ! to password
# output the value of password

words = input()
password = ""

for word in words:
    if word == "i":
        password += "1"
    elif word == "a":
        password += "@"
    elif word == "m":
        password += "M"
    elif word == "B":
        password += "8"
    elif word == "s":
        password += "$"
    else:
        password += word

password += "!"
print(password)
