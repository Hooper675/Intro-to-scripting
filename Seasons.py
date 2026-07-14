input_month = input()
input_day = int(input())
""" Type your code here. """
valid_months = ["January", "February", "March", "April", "May",
                "June", "July", "August", "September", "October",
                "November", "December"]

if input_month not in valid_months:
    print("Invalid")
elif (input_day < 1) or (input_day > 31):
    print("Invalid")
elif input_month == "September" and input_day == 31:
    print("Invalid")
else:
    if ((input_month == "March" and input_day >= 20) or
        (input_month in ["April","May"]) or
        (input_month == "June" and input_day <= 20)):
       print("Spring")

    elif ((input_month == "June" and input_day >= 20) or
          (input_month in ["July", "August",]) or           #Check for Summer
          (input_month == "September" and input_day <= 21)):
       print("Summer")

    elif((input_month == "September" and input_day >= 22) or
         (input_month in ["October","November"]) or
         (input_month == "December" and input_day <= 20)):
       print("Autumn")

    else:
        print ("Winter")