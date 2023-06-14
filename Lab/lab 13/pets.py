"""CS 108 Lab 13.0

This module implements an pets hierarchy that includes dogs and cats.

@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015
@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""


class Pet:
    """This class implements the base class from which all specific pet
    classes are derived.
    """

    def __init__(self, name='', genus=''):
        """Instantiates an pet object"""
        self.name = name
        self.genus = genus


class Dog(Pet):

    def __init__(self, name='', bites=True):
        """Instantiates an pet object"""
        Pet.__init__(self, name, 'canis')
        self.bites = bites

    def get_sound(self):
        """Returns the sound made by the dog"""
        return 'woof'
    
    def get_sound_meaning(self):
        """Returns the meaning of the sound."""
        return 'Hello, I\'m a dog and my name is ' + self.name + '.'


class Cat(Pet):

    def __init__(self, name='', lives=9):
        """Instantiates an pet object"""
        Pet.__init__(self, name, 'felis')
        self.lives = lives

    def get_sound(self):
        """Returns the sound made by the cat"""
        return 'meow'

    def get_sound_meaning(self):
        """Returns the meaning of the sound."""
        return 'Hello, I\'m a cat and my name is ' + self.name + '.'

class Flea(Pet):
    
    def __init__(self, name=''):
        """Instantiates an pet object"""
        Pet.__init__(self, name, 'pulex')

    def get_sound(self):
        """Returns the sound made by the flea"""
        return 'zzz'

    def get_sound_meaning(self):
        """Returns the meaning of the sound."""
        return 'Hello, I\'m a flea and my name is ' + self.name + '.'