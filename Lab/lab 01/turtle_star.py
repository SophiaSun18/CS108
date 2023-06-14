"""CS 108 - Lab 1.2

This program is going to draw a five-pointed star using turtle.
Delete the second @author line if working solo.

@author: ZeAi Sun (zs35)
@author: Samuel Fincher (smf39)
@date: Fall, 2021
"""

import turtle

# Start the turtle window in the corner of the screen (helpful for dual monitor).
# turtle.setup(width=800, height=600, startx=100, starty=100)

window = turtle.Screen()
pen = turtle.Turtle()

# Draw a line segment.
pen.forward(250)
pen.right(144)
pen.forward(250)
pen.right(144)
pen.forward(250)
pen.right(144)
pen.forward(250)
pen.right(144)
pen.forward(250)

# window.mainloop() # Needed for some IDEs.
