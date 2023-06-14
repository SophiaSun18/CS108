"""CS 108 - Lab 6.2

This program defines a function which returns all the unique words in the text.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

def get_unique_words(str_list):            # Define the function which asks for the list to search.
    unique_words = []                      # Create an empty list to store the unique words.
    for i in str_list:                     # Set up the loop to go through all the words in the list.
        if i not in unique_words:          # Set up the If branch to gather all the new words and put them into the empty list.
            unique_words.append(i)
    return unique_words                    # Return the result of all unique words.