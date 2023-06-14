"""CS 108 - Lab 7.3

This program defines a function to verify if a given credit card number is valid.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

# Define a new function to verify if the first characters of the given input is valid.
def is_valid_prefix(card_num):
    if (card_num[:2] == '37') or (card_num[0] == '4' or '5' or '6'):
        return True                              # If the first characters of the number is 37, 4, 5 or 6, return True.
    else:
        return False                             # If the first characters of the number is not 37, 4, 5 or 6, return False.

# Define a new function to add all digits in the odd places from right to left in the given string.
def sum_of_odds(card_num):
    list = []                                    # Create an empty list to store all the elements in the string.
    sum = 0                                      # Set up a new variable to calculate for the sum of all elements in the odd places.
    
    for i in card_num:                           # Set up a for loop to go through all elements in the string.
        list.append(int(i))                          # Turn the string elements into integers, then put them in the list.
        
    for x in range(-len(list), 0):               # Set up a for loop to go through all elements in odd places from right to left using index.
        if x % 2 == 1:                               # If the index divided by 2 remains 1, the element is in the odd place.
            sum += list[x]                               # Add the element to the sum.
            
    return sum                                   # Return the sum of all elements in odd places from right to left.

# Define a new function to double and add all digits in the even places from right to left in the given string.
def sum_of_double_evens(card_num):
    list = []                                    # Create an empty list to store all the elements in the string.
    list_even = []                               # Create an empty list to store all elements in even places in the string.
    sum = 0                                      # Set up a new variable to calculate for the sum of all elements in the even places after doubling.

    for i in card_num:                           # Set up a for loop to go through all elements in the string.
        list.append(int(i))                          # Turn the string elements into integers, then put them in the list.
        
    for x in range(-len(list), 0):               # Set up a for loop to go through all elements in odd places from right to left using index.
        if x % 2 == 0:                               # If the index divided by 2 remains 0, the element is in the odd place.
            list_even.append(list[x] * 2)                # Double the element and put the result in list_even.
            
    for a in list_even:                          # Set up a for loop to go through all elements in list_even.
        if a >= 10:                                  # Check if the element is larger than 10.
            for b in str(a):                             # If the element is larger than 10, turn it into a string and go through all elements in it.
                sum += int(b)                                # Add each digits of this double-digit number to the sum.
        else:                                        # If the element is less than 10, add it to the sum.
            sum += a
            
    return sum                                   # Return the sum.

# Define a new function to verify if the given credit card number is valid.
def is_valid_cc(cc):
    if is_valid_prefix(cc) and (13 <= len(cc) <= 16) and cc.isdigit() and ((sum_of_odds(cc) + sum_of_double_evens(cc)) % 10 == 0):
           return True                           # If the is_valid_prefix() function returns True,
                                                 #    the length of the input is between 13 and 16 characters,
                                                 #    the input has only numeric digit characters,
                                                 #    the sum_of_odds + the sum_of_double_evens is divisible by 10,
                                                 #    return True.
    else:
        return False                             # If the input doesn't fulfill all conditions, return False.