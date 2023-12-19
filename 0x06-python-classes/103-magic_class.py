#!/usr/bin/python3

""" Defines a MagicClass that does exactly the same as bytecode"""

import math

class MagicClass:
    """Representing a circle"""

    def __init__(self, radius=0):
        """ Initiate a new square
        
        Arge:
            size (int): The size of the new Square
            position (int, int): The position of the new sqaure.
       """
        self.__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
