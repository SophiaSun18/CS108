"""CS 108 Lab 12

This module tests some of the basic particle functionality.

@author: Keith VanderLinden (kvlinden)
@date: Spring, 2021
"""

from particle import Particle


# These two particles should hit and bounce.
p1 = Particle(0, 0, 1, 0, radius=50)
p2 = Particle(0.0001, 99.99, -1, 0, radius=50)
assert p1.hits(p2)
p1.bounce(p2)
assert p1.vel_y < 0
assert p2.vel_y > 0

# These two particles should not hit (or bounce).
p1 = Particle(0, 0, 1, 0, radius=50)
p2 = Particle(100, 100, -1, 0, radius=50)
assert not p1.hits(p2)
