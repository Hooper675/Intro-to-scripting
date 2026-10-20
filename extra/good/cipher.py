
# user_input = prompt inputs
# empty text variable
#while prompt_user provide a negative number or greater than 25:
# prompt_user to enter a correct digit.
#break
#    for each character in user_input:
                  #if each character is alphabet:
#the code variable appends(+=)chr((ord(i) + prompt))
#if code is more than the number of the letter z:
#minus 26 from the code variable
#otherwise add that character to text.
#print(text)

user_input = input("Enter letters and numbers:")
text = ""
prompt_user = int(input("Choose 1-25:"))

while prompt_user < 1 or prompt_user > 25:
    prompt_user = int(input("Choose 1-25:"))
    if (prompt_user >= 1) and (prompt_user <= 25):
        break
for i in user_input:
    if i.isalpha():
        code = ord(i) + prompt_user
        if i.isupper() and code > ord('Z'):
            code -=26
        elif i.lower and code < ord('z'):
            code -=26
        text += chr(code)
    else:
        text += i
print(text)