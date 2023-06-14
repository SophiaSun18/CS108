"""CS 108 Homework 6

This module implements a model of a square.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

class Square:
    """ Square models a single square that may be rendered to a canvas. """

    def __init__(self, x=50, y=50, r=10, color="brown"):
        """Instantiate a square object."""
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def draw(self, drawing):
        """Receive a drawing canvas and draw the square."""
        self.drawing = drawing
        drawing.rectangle(self.x - self.r, self.y - self.r,
                          self.x + self.r, self.y + self.r,
                          color=self.color)