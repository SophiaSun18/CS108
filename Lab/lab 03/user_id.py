"""CS 108 - Lab 3.1

This program is used to construct user ids.

@author: ZeAi Sun (zs35)
@author: Simon Detmer (sed38)
@date: Fall, 2021
"""

# Get the student input of first name, last name and student id.
first_name = input('First name: ')
last_name = input('Last name: ')
stu_id = input('Student ID: ')

# Extract information from the student input and create the user id.
user_id = first_name[0] + last_name + stu_id[0: 2]
user_id = user_id.lower()
print('User ID:', user_id)