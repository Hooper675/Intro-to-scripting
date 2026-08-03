user_input = input()
#convert number to float using float function after split a string of numbers
non_negative_number = [float(i) for i in user_input.split()]


#creating a holder for max numbers
max_number = 0

for number in non_negative_number:
    if number > max_number:
        max_number = number

average = sum(non_negative_number) / len(non_negative_number)

print(f"{max_number:.2f} {average:.2f}")