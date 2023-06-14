"""CS 108 - Lab 4.2

This program is used to calculate the day of the week.

@author: Stella Kim (sk98)
@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

# Get values for the year, month and day from the user.
year = int(input('Enter year: '))
month = int(input('Enter month: '))
day = int(input('Enter day: '))

# Convert the January and February into months 13 and 14 of the previous year.
if month == 1:
    month = 13
    year -= 1
elif month == 2:
    month = 14
    year -= 1

# Compute h.
h = (day + (((month + 1) * 26 )// 10) + (year % 100) + ((year % 100) // 4) + ((year // 100) // 4) + (5 * (year // 100))) % 7

# Create a list for the days of the week and get the result.
list = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(list[h])