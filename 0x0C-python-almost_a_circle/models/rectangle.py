#!/usr/bin/python3
""" Define a Rectangle class that inherits from base class.

"""

from models.base import Base


class Rectangle(Base):
    """ Describes a Rectangle.

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes object.

        Args:
            width (int): Width of Rectangle
            height (int): Height of Rectangle
            x (int): Position on x axis
            y (int): Position on y axis
            id (int): Id of object
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Gets width of object.
            Sets width of object.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height of object.
            Sets the height of object.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Gets the position(x) of object.
            Sets the position(x) of object.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Gets the position(y) of object.
            Sets the posiyion(y) of object.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculates the area of Rectangle """
        return self.__width * self.__height

    def display(self):
        """ Display Rectangle """
        i = 0
        print('\n' * self.__y, end='')
        while i < self.__height:
            print(' ' * self.__x + '#' * self.__width)
            i += 1

    def __str__(self):
        """ String Representation of object """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """ Update the attributes of the object """
        if len(args) >= 1:
            self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
                if len(args) >= 3:
                    self.__height = args[2]
                    if len(args) >= 4:
                        self.x = args[3]
                        if len(args) == 5:
                            self.y = args[4]
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs['id']
                if key == 'width':
                    self.width = kwargs['width']
                if key == 'height':
                    self.height = kwargs['height']
                if key == 'x':
                    self.x = kwargs['x']
                if key == 'y':
                    self.y = kwargs['y']

    def to_dictionary(self):
        """ A dictionary Representation of object """
        obj_dict = {}
        obj_dict['id'] = self.id
        obj_dict['x'] = self.x
        obj_dict['y'] = self.y
        obj_dict['width'] = self.width
        obj_dict['height'] = self.height

        return obj_dict
