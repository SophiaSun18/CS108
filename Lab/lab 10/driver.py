"""CS 108 Lab 10

This driver uses the Employee class to compute and save corporate statistics.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

from employee import Employee

employees = []

# Construct an employee object for each employee specified in 'employees.txt'
# and add it to the employees list.

openfile = open('employees.txt')
lines = openfile.readlines()
for l in lines:
    value = l.split(',')
    employee = Employee(value[0], value[1], value[2], int(value[3]))
    employees.append(employee)

# Write the total number of employees into the 'employee-count.txt' file.
numfile = open('employee-count.txt', 'w')
numfile.write(str(len(employees)))
numfile.close()

# Compute and print out statistics for employees.

# Print a message if there are no employees.
if len(employees) == 0:
    print("There's no employee information.")

# Create dictionaries for the total number of employees in a given rank and the sum of all salaries of the rank.
else:
    totals = {}
    counts = {}
    max_employee = employees[0]
    min_employee = employees[0]
    
    for employee in employees:
        
        # Decide if the rank of the employee is included in the totals dictionary.
        if employee.rank in totals:
            # Increment the value for the rank.
            totals[employee.rank] += employee.salary
            counts[employee.rank] += 1
        else:
            # Create new entry for the rank.
            totals[employee.rank] = employee.salary
            counts[employee.rank] = 1
            
        # Decide if the salary of the employee is greater than the maximum salary and update the maximum salary.
        if employee.salary > max_employee.salary:
            max_employee = employee
        
        # Decide if the salary of the employee is less than the minimum salary and update the minimum salary.
        if employee.salary < min_employee.salary:
            min_employee = employee

# Write statistics into a new file.
f = open('employee-stats.txt', 'w')
f.write('Maximum and Minimum Salaries\n')
f.write(str(max_employee))
f.write('\n')
f.write(str(min_employee))
f.write('\n')
f.write('Rank and Average Salaries\n')

for rank in totals:
    f.write(rank + ': {:.2f}'.format(totals[rank] / counts[rank]))
    f.write('\n')

f.close()