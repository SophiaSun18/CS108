"""CS 108 - Lab 6.1

This program defines a function which searchs for a target word in a list and return the index of its first occurrence.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

def search(str_list, target=' '):      # Define the function which asks for the list to search and the target.
    for i in range(len(str_list)):     # Set up the repitition for all elements in the target list.
        if target == str_list[i]:      # Search for the target in the list by going through all indexs.
            return i                   # Return the position of the target's first occurrence.
    return -1                          # Return -1 if the target isn't found in the list.