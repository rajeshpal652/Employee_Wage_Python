import random

wage_per_hour = 20
full_day_hour = 8

empCheck = random.randint(0,1)
if(empCheck == 0):
    print("Employee is Absent")
    print("Daily Employee Wage : ", 0)
else:
    print("Employee is Present")
    print("Daily Employee Wage : ", wage_per_hour * full_day_hour)