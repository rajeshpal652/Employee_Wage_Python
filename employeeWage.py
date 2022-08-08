import random

wage_per_hour = 20
full_day_hour = 8
part_time_hour = 4

is_absent = 0
is_present = 1
is_part_time = 2

empCheck = random.randint(0,2)
if(empCheck == is_absent):
    print("Employee is Absent")
    print("Daily Employee Wage : ", 0)
elif(empCheck == is_present):
    print("Employee is Present")
    print("Daily Employee Wage : ", wage_per_hour * full_day_hour)
else:
    print("Employee is working Part Time")
    print("Daily Employee Wage : ", wage_per_hour * part_time_hour)