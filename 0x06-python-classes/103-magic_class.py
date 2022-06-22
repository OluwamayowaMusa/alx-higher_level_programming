#!/usr/bin/python3

""" A module which defines the MagicClass.

"""
import math


class MagicClass:
    """ Describes a circle.

    """

    def __init__(self, radius=0):
        self.__radius = 0
        """ Initializes the object with radius.

        Args:
            radius (int, float): Radius of circle
        """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """ Calculates the area of circle """
        return (self.__radius ** 2) * math.pi

    def cicumference(self):
        """ Calculates the circumference of circe """
        return 2 * math.pi * self.__radius
