"""CS 108 - Lab 7.1

This program defines a function to verify if an input string is a valid SSN.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

# Define a new function to verify whether the input string is a valid SSN.
def is_valid_ssn(ssn):
    if len(ssn) == 11:              # Set up an if-else statement to check if the input string has the right length of 11.
        if (ssn[:3].isdigit() and ssn[4:6].isdigit() and ssn[7:].isdigit()) and (ssn[3] and ssn[6] == '-'):
            return True             # If the string has the right length, then check if it has the right format 'ddd-dd-dddd' which each d indicates a digit.
        else:
            return False            # If the format of the string is not 'ddd-dd-dddd', then return False.
    else:
        return False                # If the length of the string is not 11, then return False.