"""CS 108 - Homework 1.0

This module draws a French flag.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

# Import turtle and set up the canvas and pen
import turtle
turtle.setup(width=1400, height=1000)
pen = turtle.Turtle()

# Set up the scale factor
Scale_factor = int(input('Input: '))

# Draw the left blue part of the flag
pen.color('#0055A4')
pen.begin_fill()
pen.forward(Scale_factor)
pen.left(90)
pen.forward(Scale_factor * 2)
pen.left(90)
pen.forward(Scale_factor)
pen.left(90)
pen.forward(Scale_factor * 2)
pen.end_fill()

# Put the pen to the proper position
pen.left(90)
pen.forward(Scale_factor)

# Draw the middle white part of the flag
pen.color('#000000')
pen.forward(Scale_factor)
pen.left(90)
pen.forward(Scale_factor * 2)
pen.left(90)
pen.forward(Scale_factor)

# Put the pen to the proper position
pen.right(180)
pen.forward(Scale_factor)

# Draw the right red part of the flag, then hide the pen
pen.color('#EF4135')
pen.begin_fill()
pen.forward(Scale_factor)
pen.right(90)
pen.forward(Scale_factor * 2)
pen.right(90)
pen.forward(Scale_factor)
pen.end_fill()

pen.hideturtle()