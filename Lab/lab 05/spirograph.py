"""CS 108 - Lab 5.2

This program draws spirograph based on user's input.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

from guizero import App, Drawing
import math

app = App('Drawing Canvas')

drawing = Drawing(app, width='fill', height='fill')

# Get inputs from the user.
r = float(input('moving radius: '))
R = float(input('fixed_radius: '))
p = float(input('pen_offset: '))
color = str(input('color: '))
center = app.width / 2

# Set up the initial x and y for the spirograph.
x = R + r + p + center
y = 0.0 + center

# Draw the spirograph.
t = 0.0
while t < 360:
    t += 0.1
    next_x = (R + r) * math.cos(t) + p * math.cos(((R + r) * t)/r) + center
    next_y = (R + r) * math.sin(t) + p * math.sin(((R + r) * t)/r) + center
    drawing.line(x, y, next_x, next_y, color=color)
    x = next_x
    y = next_y

app.display()