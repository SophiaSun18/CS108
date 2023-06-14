"""CS 108 Homework 6

This module implements a GUI controller for a pop-up window simulation

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Fall, 2018 - updated to use callback animation
@date: Spring, 2021 - ported to GuiZero
@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

from guizero import App, Drawing, PushButton, Box
from helpers import get_random_color, distance
from random import randint
from particle import Square

class Square_Simulation:
    """Square_Simulation runs a simulation of multiple squares popping up a single canvas."""

    def __init__(self, app):
        """Instantiate the simulation GUI app."""

        app.title = 'Square Simulation'
        app.width = 500
        app.height = 550
        
        box = Box(app, width=500, height=550, layout='grid')
        
        self.drawing = Drawing(box, width=500, height=500, grid=[0,0,2,1])
        self.drawing.bg='black'
        
        PushButton(box, text='Clear', command=self.clear_all, grid=[0,1])
        PushButton(box, app.destroy, text='Quit', grid=[1,1])
        
        app.repeat(25, self.draw_frame)
        
        self.s_list = []
        
        self.drawing.when_clicked = self.clear_all

    def draw_frame(self):
        """Draw a new square."""
        self.drawing.clear()
        
        self.add_square()
        
        for s in self.s_list:
            s.draw(self.drawing)
        
    def add_square(self):
        """Add a new square to the canvas."""
        self.square = Square()
        
        self.square.r = randint(5, 40)
        self.square.x = randint(40, (self.drawing.width - 40))
        self.square.y = randint(40, (self.drawing.height - 40))
        
        self.square.color = get_random_color()
        
        self.s_list.append(self.square)
                
    def clear_all(self):
        """Remove all squares and clear the canvas."""
        self.s_list.clear()

app = App()
Square_Simulation(app)
app.display()