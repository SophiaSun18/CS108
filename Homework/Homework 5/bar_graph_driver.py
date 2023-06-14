"""CS 108 - Homework 5.0

This driver uses the BarGraph class to draw bargraph based on an outside data list.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

# Import necessary libraries.
from bar_graph import BarGraph

from guizero import App, Drawing
app = App('Bar Graph')
drawing = Drawing(app, width='fill', height='fill')

import random

# Define two new functions for drawing the bargraph.
def get_random_color():
    '''This function gets a random color.'''
    return random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def get_data():
    '''This function reads data from a txt file and outputs the values in a list.'''
    filename = input('Filename: ')
    f = open(str(filename), 'r')
    list = f.read().split('\n')
    data = []
    for i in list:
        if i != '':
            data.append(int(i))
    f.close()
    return data

# Construct a new bargraph object and draw the bargraph.
bg = BarGraph(get_data(), get_random_color())
bg.draw(drawing)