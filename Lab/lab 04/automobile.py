"""CS 108 - Lab 4.0

This program prompts the user for an automobile service.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

# Get the customer input of certain survice.
service = input('service: ')

# Set up the if-else branches and output the price of the service.
if service == 'oil change':
    print('cost of oil change: $35')
elif service == 'tire rotation':
    print('cost of tire rotation: $19')
elif service == 'car wash':
    print('cost of car wash: $7')
else:
    print('error:', service, 'is not recognized')