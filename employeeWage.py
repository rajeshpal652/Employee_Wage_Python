import random

wage_per_hour = 20
days_per_month = 20

is_absent = 0
is_present = 1
is_part_time = 2


dayCount = 1
empHrs = 0
totalEmpWage = 0
empWage = 0

while (dayCount <= days_per_month):
    empCheck = random.randint(0, 2)
    if (empCheck == is_absent):
        empHrs = 0
    elif (empCheck == is_present):
        empHrs = 8
    else:
        empHrs = 4

    dayCount = dayCount + 1
    empWage = wage_per_hour * empHrs
    totalEmpWage += empWage
    print("Total Employee Wage of the day : ", totalEmpWage)

print("Total employee wage of the month : ", totalEmpWage)