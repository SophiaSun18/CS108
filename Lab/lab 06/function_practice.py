"""CS 108 - Lab 6.0

This program writes two functions which calculate for the cost of a raod trip and the number of spaces in a string respectively.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

# Writes a new function which calculates for the cost of a road trip.
def compute_cost(miles, miles_per_gallon, dollars_per_gallon):
    return((miles / miles_per_gallon) * dollars_per_gallon)

# Writes a new function which calculates for the number of spaces in an input string.
def count_spaces(s):
    count = 0
    for i in s:
        if i == ' ':
            count += 1
    return count