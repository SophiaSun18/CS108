"""CS 108 Lab 11.1

This modules runs some tests on the calculator class.

It uses the assert command, which verifies that the given boolean expression
returns True. If not, it raises and exception.

@author: Serita Nelesen (smb4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015 - replaced JUnit tests with assert tests
@date: Spring, 2020 - ported to ZyLabs
@date: Spring, 2021 - factored out the tests

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

from calculator import Calculator


# Use this (one) calculator to run all the tests.
calc = Calculator()

# These addition tests should run without raised exceptions.
assert calc.calculate('0', '+', '1') == 1
assert calc.calculate('-7', '+', '9') == 2
assert calc.calculate('-4', '+', '-8') == -12
assert calc.calculate('3', '+', '0') == 3
assert calc.calculate('2.0', '+', '5.3') == 7.3

# These subtraction tests should run without raised exceptions.
assert calc.calculate('3', '-', '9') == -6
assert calc.calculate('-4', '-', '-8') == 4
assert calc.calculate('-7', '-', '9') == -16
assert calc.calculate('3', '-', '0') == 3
assert calc.calculate('2.0', '-', '5.3') == -3.3

# These multiplication tests should run without raised exceptions.
assert calc.calculate('3', '*', '9') == 27
assert calc.calculate('-4', '*', '-8') == 32
assert calc.calculate('-7', '*', '9') == -63
assert calc.calculate('3', '*', '0') == 0
assert calc.calculate('2.0', '*', '5.3') == 10.6

# These division tests should run without raised exceptions.
# We don't check division by zero.
assert calc.calculate('3', '/', '12') == 0.25
assert calc.calculate('-4', '/', '-8') == 0.5
assert calc.calculate('16', '/', '-8') == -2
assert calc.calculate('0', '/', '3') == 0
assert calc.calculate('-5.0', '/', '2') == -2.5

# Test the calculator memory.
calc.set_memory(2)
assert calc.calculate('M', '+', '1') == 3
assert calc.calculate('2', '*', 'M') == 4
assert calc.calculate('2', '*', '3') == 6

# If we get this far, the tests must have all passed.
print('tests passed!')
