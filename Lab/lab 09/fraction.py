"""CS 108 - Lab 9.1

This module implements a new class which has attributes related to fraction calculation.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

import math

class Fraction:
    
    def __init__(self, numerator, denominator):
        '''Receives two arguments and stores them to construct a new fraction.'''
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
    
    def __str__(self):
        '''Receives self and returns a string in the format 'numerator/denominator'.'''
        return str(self.numerator) + '/' + str(self.denominator)
    
    def is_valid(self):
        '''Tests if the given fraction is valid (the denominator is not zero) and returns a Boolean value.'''
        return self.denominator != 0
    
    def simplify(self):
        '''Simplifies the given fraction.'''
        gcd = math.gcd(self.numerator, self.denominator)
        if gcd != 0:                                     # If the numerator and the denominator have a gcd, divide both of them with the gcd to simplify the fraction.
            self.numerator = self.numerator // gcd
            self.denominator = self.denominator // gcd
        if self.denominator < 0:                         # If the denominator is negative, change the denominator to a positive one.
            self.numerator = self.numerator * (-1)
            self.denominator = self.denominator * (-1)
    
    def __mul__(self, other):
        '''Receives a new fraction object and multiply the original fraction object with the new one.'''
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)
    
    def get_decimal(self):
        return float(self.numerator / self.denominator)

f = Fraction(3,3)
print(f.get_decimal())