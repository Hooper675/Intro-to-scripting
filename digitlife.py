
user_input = input("Enter MMDDYYYY for your DOB:")

new_input = 0
sum_digit = 0
for i in user_input:
    if i.isdigit():
        new_input += int(i)
    else:
        continue
while new_input >= 9:
    new_num = [int(j)for j in str(new_input)]
    new_input = sum(new_num)


print(new_input)
