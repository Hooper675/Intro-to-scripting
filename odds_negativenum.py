size = 5


def get_numbers(num):
    numbers = []
    print(f"Enter {num} integers")
    for i in range(num):
        number = int(input(f"Enter number {i + 1}: "))  # Convert string input to integer
        numbers.append((number))  # Add to numbers list
    return numbers


def print_all_numbers(numbers):
    print("Numbers:", *numbers)  # This should output all of the numbers in the numbers variable.
    # * will inpack the values stored in variable numbers


def print_odd_numbers(numbers):
    odd_numbers = []
    for num in numbers:
        if num % 2 != 0:
            odd_numbers.append(num)
    print("Odd numbers:", *odd_numbers)


def print_negative_numbers(numbers):
    for j in numbers:
        if j < 0:
            print(f"Negative numbers: {j}")


nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)