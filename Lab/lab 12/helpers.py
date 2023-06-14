"""CS 108 Lab 12

This module implements helper functions for lab 12.

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author Ken Arnold (ka37): updated to use hex format strings
@date: Fall 2020
"""

from random import randint


def get_random_color():
    """Generate random color intensities for red, green and blue, and
    convert them to hex.
    """
    return '#{:02X}{:02X}{:02X}'.format(
        randint(0, 255),
        randint(0, 255),
        randint(0, 255)
    )


def distance(x1, y1, x2, y2):
    """ Compute the distance between two points. """
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5