"""CS 108 - Lab 9.0

This module implements a simple food item class with nutritional information.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

class FoodItem:

    def __init__(self, name, fat, carbohydrates, protein):
        """Constructs a FoodItem instance with the given attributes"""
        self.name = name
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.protein = protein

    def __str__(self):
        """Returns a printable representation of this food item"""
        return (
            self.name
            + "\n\tFat: {:.2f} g".format(self.fat)
            + "\n\tCarbohydrates: {:.2f} g".format(self.carbohydrates)
            + "\n\tProtein: {:.2f} g".format(self.protein)
        )

    def get_calories(self, num_servings):
        """Returns the number of calories for the given number of servings of
        this food item
        """
        return num_servings * (
            (self.fat * 9) + (self.carbohydrates * 4) + (self.protein * 4)
        )

# Instantiates new FoodItem objects for M&Ms and water.
item_MM = FoodItem('M&Ms', 10, 34, 2)
calo_M = item_MM.get_calories(1)
item_water = FoodItem('Water', 0, 0, 0)
calo_w = item_water.get_calories(10)

# Print the output.
print(item_MM)
print('Calories per serving:', float(calo_M))
print()
print(item_water)
print('Calories per 10 servings:', float(calo_w))