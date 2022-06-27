#!/usr/bin/python3
""" A module which defines a class Rectangle.

"""


class Rectangle:
    """ Describes a Rectangle.

    Attributes:
        number_of_instances (int): A counter for the number of instances
        print_symbol (int, str ...): A symbol for representation of rectangle

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initializes the object.

        Args:
            width (int): Width of Reactangle
            height (int): Height of Rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Gets the width of Rectangle. Raises TypeEror
        if width is not an integer, ValueError if width is
        not >= 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height of rectangle. Raises TypeError
        if height is not an integer, ValueError if height is
        not >= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates the area of reactangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ String representation of object """
        if self.__width == 0 or self.__height == 0:
            return ""
        _s = ""
        i = 0
        while i < self.__height:
            _s += (str(self.print_symbol) * self.__width + '\n')
            i += 1
        return _s[:-1]

    def __repr__(self):
        """ Canonical String Representation of the object """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Delete the existing object """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares the rectangles based on area.

        Args:
            rect_1 (Rectangle): First Rectangle
            rect_2 (Rectangle): Second Rectangle

        Returns:
            The Biggest Rectangle or rect_1 if both have equal area

        Raises:
            TypeError if rect_1 or rect_2 is not an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Defines a square using classmethod(decorator).

        Args:
            size (int): Size(width or height) of square

        Return:
            A rectangle instance with width==height==size
        """
        return cls(size, size)
