# Client1


from oop_getting_deeper2.Example01.EmployeeTypes import *
from oop_getting_deeper2.Example01.PayrollProcessor import *

management_employee_1 = FullTimeManagementEmployee("John", "Papa", 1001, 5, 120000.00)
salaried_employee_1 = FullTimeSalariedEmployee("Kari", "Smith", 2001, 1, 60000.00)
sales_employee_1 = FullTimeSalariedSalesEmployee("Jake", "Miller", 1004, 10, 80000.00, 5)

lis_of_employees = [management_employee_1, salaried_employee_1, sales_employee_1]

payroll = PayrollProcessor("07/01/2020")
payroll.print_payroll_report(lis_of_employees)
payroll.print_annual_bonus_report(lis_of_employees)

