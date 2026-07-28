# defined function takes in the values from user input and then swap the values
def swap_values(val1, val2, val3, val4):
    val1, val2 = val2, val1
    val3, val4 = val4, val3
    return val1, val2, val3, val4


# this part of the script is used to check how the script is being run whether it's being import or not.
if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    print(*swap_values(num1, num2, num3, num4))