"""CS 108 - Homework 2.0

This module draws two circles and determine their relative position based on user's input.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

# Import math and Guizero and set up the screen.
import math
from guizero import App, Drawing

app = App('Drawing Canvas', width = 1000, height = 1000)

d = Drawing(app, width = 1000, height = 1000)

# Get user input for both circles.
x1 = int(input('Circle 1 x: '))
y1 = int(input('Circle 1 y: '))
r1 = int(input('Circle 1 radius: '))

x2 = int(input('Circle 2 x: '))
y2 = int(input('Circle 2 y: '))
r2 = int(input('Circle 2 radius: '))

# Draw the circles.
d.oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, outline = True, color = 'white')
d.oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, outline = True, color = 'white')

# Calculate for the distance of centers and decide the relative position of the circles.
dis_c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if dis_c >= (r1 + r2):
    print('The circles are disjoint.')
    d.text(150, 150, 'The circles are disjoint.')

elif abs(r1 - r2) <= dis_c < r1 + r2:
    print('The circles overlap.')
    d.text(150, 150, 'The circles overlap.')

else:
    if r1 > r2:
        print('Circle 1 contains circle 2.')
        d.text(150, 150, 'Circle 1 contains circle 2.')
    elif r2 > r1:
        print('Circle 2 contains circle 1.')
        d.text(150, 150, 'Circle 2 contains circle 1.')

app.display()