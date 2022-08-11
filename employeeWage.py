import random

class EmployeeWage():
    wage_per_hour = 20
    days_per_month = 20
    max_total_working_hrs = 100

    is_absent = 0
    is_present = 1
    is_part_time = 2

    dayCount = 1
    empHrs = 0
    totalEmpWage = 0
    empWage = 0
    totalEmpHrs = 0

    def wageCount(self):
        while self.dayCount <= self.days_per_month and self.totalEmpHrs <= self.max_total_working_hrs:
            empCheck = random.randint(0, 2)
            if (empCheck == self.is_absent):
                self.empHrs = 0
            elif (empCheck == self.is_present):
                self.empHrs = 8
            else:
                self.empHrs = 4

            self.dayCount = self.dayCount + 1
            self.empWage = self.wage_per_hour * self.empHrs
            self.totalEmpWage += self.empWage
            self.totalEmpHrs += self.empHrs
            print("Total Employee Wage of the day : ", self.totalEmpWage, " Day No : ", self.dayCount - 1)

        print("Total employee wage of the month : ", self.totalEmpWage)

empWage = EmployeeWage()
empWage.wageCount()
