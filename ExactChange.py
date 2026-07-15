total_change = int(input())

if total_change <= 0:
    print("No change")
else:
    #Calculate the dollar
    dollars = total_change // 100
    total_change = total_change % 100

    #Calculate quarter
    quarters = total_change // 25
    total_change = total_change % 25

    #Calculate dimes
    dimes = total_change // 10
    total_change = total_change % 10

    #Calculate nickles
    nickels = total_change // 5
    total_change = total_change % 5

    pennies = total_change

    if dollars > 1:
        print(f"{dollars} Dollars")
    elif dollars == 1:
        print(f"{dollars} Dollar")

    if quarters > 1:
        print(f"{quarters} Quarters")
    elif quarters == 1:
        print(f"{quarters} Quarter")

    if dimes > 1:
        print(f"{dimes} Dimes")
    elif dimes == 1:
        print(f"{dimes} Dime")

    if nickels > 1:
        print(f"{nickels} Nickels")
    elif nickels == 1:
        print(f"{nickels} Nickel")

    if pennies > 1:
        print(f"{pennies} Pennies")
    elif pennies == 1:
        print(f"{pennies} Penny")
