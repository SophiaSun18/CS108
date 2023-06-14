"""CS 108 - Lab 5.1

This program takes a positive integer input from the user and convert it into a binary number.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

# Get a positive input from the user.
x = int(input('integer: '))

# Convert the input into a binary number.
while x > 0:
    print(x % 2, end = '')
    x = x // 2
print()