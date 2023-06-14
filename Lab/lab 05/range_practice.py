"""CS 108 - Lab 5.0

This program is used to output integers with an increment of 10.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

# Get two inputs from the user.
a = int(input())
b = int(input())

# Output the new integer with an increment of 10.
if b < a:
    print("Second integer can't be less than the first.")
else:
    while a <= b:
        print(a)
        a += 10