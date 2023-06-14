"""CS 108 - Lab 7.2

This program defines a function to verify if the given password is a valid password.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

def is_valid_password(password):             # Define a new function to verify the given input.
    
    num_digit = 0                            # Set up a new variable to count the number of digits in the password.
    
    if len(password) >= 8:                   # Check if the length of the password is longer than 8. If it's longer, proceed to further verification.
        
        for i in password:                       # Set up a for loop to check every element in the password.
            if not i.isalnum():
                return False                         # If any element in the password is neither a number nor a letter, return False.
            else:                                    # If every element in the password is a number or a letter, proceed to further verification.
                if i.isdigit():
                    num_digit += 1                       # Check every element in the password. If the element is a number, add 1 to num_digit.
                    
        if num_digit >= 2:
            return True                          # If the password contains more than 2 numbers, return True.
        else:
            return False                         # If the password contains less than 2 numbers, return False.
        
    else:                                    # If the length of the password is shorter than 8, return False.
        return False