"""CS 108 - Lab 3.0

This program assigns varibales to user inputs using appropriate variable names and data types.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

# Creates a list to store the user inputs of the scores, then get the values.
scores = [int(input('score: ')), int(input('score: '))]

# Get the value of the system password.
password = input('password: ')

# Get the user inputs of the GPS coordinates while putting them into the tuple.
dorm = ((float(input('latitude: '))), (float(input('longitude: '))))

# Creates a dictionary to store the user inputs of the states, then get the values.
state_capitals = {input('state: '): input('capital: '), input('state: '): input('capital: ')}
