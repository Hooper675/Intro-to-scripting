wage = 20
wage1 = 30
total_hours_work = int(input("Enter your hours here:"))

if total_hours_work <= 40:
    total_wage = total_hours_work * wage
    print(f"Your total wage is {total_wage}")
else:
    overtime_hour_work = total_hours_work - 40
    regular_hour_work = 40
    total_wage = (regular_hour_work * wage) + (overtime_hour_work * 30)
    print(f"Your total wage is {total_wage}")
