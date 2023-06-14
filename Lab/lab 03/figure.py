"""CS 108 - Lab 3.3

This program is use to draw a stick figure using GuiZero.

@author: ZeAi Sun (zs35)
@author: Simon Detmer (sed38)
@date: Fall, 2021
"""
# Import Guizero and set up the screen.
from guizero import App, Drawing

app = App('Drawing Canvas')

drawing = Drawing(app, width='fill', height='fill')

# Change this value to rescale the drawing. 
unit = 50

# Draw the head of the stick figure in yellow.
drawing.oval(
    1 * unit, 2 * unit,  # x1, y1
    3 * unit, 4 * unit,  # x2, y2
    outline=False,
    color='yellow'
)

# Draw the body of the stick figure in blue.
drawing.line(
    1 * unit, 5 * unit,
    3 * unit, 5 * unit,
    color='blue'
)

# Draw the arms of the stick figure in red.
drawing.line(
    2 * unit, 4 * unit,
    2 * unit, 6 * unit,
    color='red'
)

# Draw the legs of the stick figure in green.
drawing.line(
    2 * unit, 6 * unit,
    1 * unit, 7 * unit,
    color='green'
)

drawing.line(
    2 * unit, 6 * unit,
    3 * unit, 7 * unit,
    color='green'
)

app.display()