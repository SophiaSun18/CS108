"""CS 108 Lab 11.1

This module provides basic functionality for a calculator.

@author: Serita Nelesen (smb4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015 - replaced JUnit tests with assert tests
@date: Spring, 2020 - ported to ZyLabs

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

class Calculator:

    def __init__(self):
        """ Initialize calculator memory to 0. """
        self.memory = 0

    def calculate(self, operand1, operator, operand2):
        """ Perform the specified calculation. No error-checking is done for
        division by zero.
        """
        if operand1 and operand2 == 'M':
            operand1 = self.memory
            operand2 = self.memory
            
        elif operand1 == 'M':
            operand1 = self.memory
            operand2 = float(operand2)
        
        elif operand2 == 'M':
            operand1 = float(operand1)
            operand2 = self.memory
        
        else:
            operand1 = float(operand1)
            operand2 = float(operand2)

        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2

    def set_memory(self, num):
        '''Reset memory to the new input.'''
        self.memory = float(num)