"""CS 108 Lab 10

This class models an employee.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""


class Employee:
    """ Represents an employee object.
    Invariant:
    - Salary is an integer.
    """

    def __init__(self, given_name='John', family_name='Doe', rank='Staff', salary=10000):
        """Instantiate a new employee object, defaulting to a basic John Doe."""
        self.given_name = given_name
        self.family_name = family_name
        self.rank = rank
        self.salary = salary

    def __str__(self):
        """Create a employee string with a simple format."""
        return self.family_name + ', ' + self.given_name + ': ' + \
               self.rank + ' ($' + str(self.salary) + ')'
