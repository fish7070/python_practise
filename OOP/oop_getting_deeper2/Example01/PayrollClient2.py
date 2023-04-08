# Client2

from oop_getting_deeper2.Example01.EmployeeTypes import *
from oop_getting_deeper2.Example01.PayrollProcessor import *

management_employee_1 = Employee("John", "Papa", 1001, 5)
salaried_employee_1 = Employee("Kari", "Smith", 2001, 1)
sales_employee_1 = Employee("Jake", "Miller", 1004, 10)

list_of_employees = [management_employee_1, salaried_employee_1, sales_employee_1]

payroll = PayrollProcessor("07/01/2020")
payroll.print_payroll_report(list_of_employees)
payroll.print_annual_bonus_report(list_of_employees)