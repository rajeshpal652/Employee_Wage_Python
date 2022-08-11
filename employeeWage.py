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

    def __init__(self, company_name, wage_per_hour, days_per_month, max_total_working_hrs):

        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.days_per_month = days_per_month
        self.max_total_working_hrs = max_total_working_hrs
        self.return_value = self.wageCount()

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
        # print(company_details_list)
        print("Total employee wage of the month : ", company_details_list[len(company_details_list)-1])
        return company_details_list

if __name__ == "__main__":
    condition = True
    company_details_list_array = []
    while(condition == True):
        print("")
        print("<=====================================Employee Wage Builder=====================================>")
        choice = int(input("1. Enter 1 to add Company Details \n2. Enter 2 to know Company Details \n3. Exit \n"))

        if(choice == 1):
            company_name = input("Enter Name of the Company : ")
            wage_per_hour = int(input("Enter Wage Per Hour : "))
            days_per_month = int(input("Enter Working Days Per Month : "))
            max_total_working_hrs = int(input("Enter Maximum Working Hours Per Month : "))
            employeePayroll = EmployeePayroll(company_name, wage_per_hour, days_per_month, max_total_working_hrs)
            company_details_list_array.append(employeePayroll.return_value)

        elif(choice == 2):
            company = input("Enter Company name to find Employee Wage details : ")
            for company_details in company_details_list_array:
                if(company in company_details):
                    print("Company Name : ", company_details[0],
                          "\nWage Per Hour : ", company_details[1],
                          "\nWorking Days Per Month : ", company_details[2],
                          "\nMaximum Working Hours Per Month : ", company_details[3],
                          "\nTotal Employee Wage per Month: ", company_details[4])

        else:
            condition = False