"""CS 108 Lab 12

This module implements a GUI controller for a particle simulation

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Fall, 2018 - updated to use callback animation
@date: Spring, 2021 - ported to GuiZero
@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

from guizero import App, Drawing, PushButton, Box
from random import randint
from particle import Particle
from helpers import get_random_color, distance


class ParticleSimulation:
    """ParticleSimulation runs a simulation of multiple particles interacting
    on a single canvas.
    """

    def __init__(self, app):
        """Instantiate the simulation GUI app."""

        app.title = 'Particle Simulation'
        UNIT = 500
        CONTROL_UNIT = 50
        app.width = UNIT
        app.height = UNIT + CONTROL_UNIT
        
        self.p_list = []

        box = Box(app, layout='grid', width=UNIT, height=UNIT + CONTROL_UNIT)
        self.drawing = Drawing(box, width=UNIT, height=UNIT, grid=[0,0,2,1])
        self.drawing.bg = "black"
        PushButton(box, text='Add particle', command=self.add_particle, grid=[0,1])
        PushButton(box, text='Clear', command=self.clear_all, grid=[1,1])
        
        app.repeat(10, self.draw_frame)
        
        self.drawing.when_clicked = self.check_remove_particle

    def draw_frame(self):
        """Draw a new particle."""
        self.drawing.clear()
        
        for p in self.p_list:
            p.move(self.drawing)
        
        for i in range(len(self.p_list)):
            for j in range(i):
                 self.p_list[i].bounce(self.p_list[j])
        
        for p in self.p_list:
            p.draw(self.drawing)
        
    def add_particle(self):
        """Add a new particle to the canvas."""
        self.particle = Particle()
        
        self.particle.radius = randint(5, 25)
        self.particle.x = randint(25, (self.drawing.width - 25))
        self.particle.y = randint(25, (self.drawing.height - 25))
        
        vel = randint((self.particle.radius * -1) // 10, (self.particle.radius // 10))
        self.particle.vel_x = vel
        self.particle.vel_y = vel
        
        self.particle.color = get_random_color()
        
        self.p_list.append(self.particle)
    
    def check_remove_particle(self, event):
        """Check if the particle is clicked and remove the clicked particle."""
        copy = self.p_list[:]
        for p in copy:
            if p.is_clicked(event.x, event.y) is True:
                self.p_list.remove(p)
                
    def clear_all(self):
        """Remove all particles and clear the canvas."""
        self.p_list.clear()

app = App()
ParticleSimulation(app)
app.display()
