"""CS 108 - Homework 5.0

This program defines necessary methods in the BarGraph class to draw a bargraph.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

# Define a new class for drawing a new bargraph.
class BarGraph:
    
    def __init__(self, data=[], color='blue'):
        '''This constructor stores the received data and color as instance variables.'''
        self.data = data
        self.color = color
    
    def __str__(self):
        '''This method returns a string representing the graph’s internal state'''
        return 'Bar Graph - Color: ' + self.color + ' Data: ' + str(self.data)
    
    def draw(self, drawing):
        '''This method returns a graph drawn based on a given list of values.'''
        
        self.drawing = drawing
        
        unit_x = drawing.master.width / max(self.data)
        unit_y = drawing.master.height / len(self.data)

        for i in range(len(self.data)):
            drawing.rectangle(
                0, unit_y * i,
                unit_x * self.data[i], unit_y * (i + 1),
                color = self.color, outline = True
                )
        
        return drawing.master.display()