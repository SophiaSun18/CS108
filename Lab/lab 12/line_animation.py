"""CS 108 Lab 12.0

This module implements a simple line animation.

@author: Keith VanderLinden (kvlinden)
@date: Spring, 2020
@date: Spring, 2021 - ported to GuiZero
@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

from guizero import App, Drawing


class LineAnimation:

    def __init__(self, app):

        app.title = 'Line Animation'

        self.width = app.width
        self.height = app.height

        self.drawing = Drawing(app, width=self.width, height=self.height)

        # Start the animation with a horizontal line from the top left.
        self.x1 = 0
        self.y1 = 0
        self.x2 = self.width
        self.y2 = 0

        # Start the animation.
        app.repeat(5, self.draw_frame)

    def draw_frame(self):
        """Draw one animation frame and set up the next."""

        # Draw the line
        self.drawing.line(self.x1, self.y1, self.x2, self.y2, color='#66CCFF')

        # Move the right coordinate down one pixel.
        # Stop the animation at the bottom right point.
        if self.y2 != self.height:
            self.y2 += 1
        else:
            self.y2 += 0


app = App()
LineAnimation(app)
app.display()
