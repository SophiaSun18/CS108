"""CS 108 - Lab 3.2

This program create a dictionary wit names and scores.

@author: ZeAi Sun (zs35)
@author: Simon Detmer (sed38)
@date: Fall, 2021
"""

# Create a dictonary called score_dict
score_dict = {'Joe': 10, 'Tom': 23, 'Barb': 13, 'Sue': 19, 'Sally': 12}

# Test printing a dictionary value and revise and print updated dictionary
print(score_dict['Barb'])
score_dict['Sally'] = 13
del score_dict['Tom']
print(score_dict)
