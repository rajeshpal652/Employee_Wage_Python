import random

class EmployeePayroll():

    is_absent = 0
    is_present = 1
    is_part_time = 2

    dayCount = 1
    empHrs = 0
    totalEmpWage = 0
    empWage = 0
    totalEmpHrs = 0
    company_details_list_array = []

    def __init__(self, company_name, wage_per_hour, days_per_month, max_total_working_hrs):

        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.days_per_month = days_per_month
        self.max_total_working_hrs = max_total_working_hrs

    def wageCount(self):

        print("<============================================================================================>")
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
            print("Employee Wage of the day : ", self.empWage,
                  " Total Employee Wage upto the Day : ", self.totalEmpWage, " Day No : ", self.dayCount - 1)

        company_details_list = [self.company_name, self.wage_per_hour,
                              self.days_per_month, self.max_total_working_hrs, self.totalEmpWage]
        self.company_details_list_array.append(company_details_list)
        print(company_details_list)
        print("Total employee wage of the month : ", company_details_list[len(company_details_list)-1])

employeePayroll1 = EmployeePayroll("Amazon",50,23,187)
employeePayroll1.wageCount()
print(employeePayroll1.company_details_list_array)
employeePayroll2 = EmployeePayroll("Google",60,20,198)
employeePayroll2.wageCount()
print(employeePayroll2.company_details_list_array)
