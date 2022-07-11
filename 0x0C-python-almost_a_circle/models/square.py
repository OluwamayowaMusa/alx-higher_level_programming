#!/usr/bin/python3
""" Defines a class Square that inherits from class Rectangle.

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Descibes a Square.

    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the object.

        Args:
            size (int): Size of sqaure
            x (int): Position on x axis
            y (int): Position on y axis
            id (int): Id of object
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ Gets the size of object.
            Sets the size of object.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__size = value
        super().__init__(value, value, self.x, self.y, self.id)

    def __str__(self):
        """ String Representation of object """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """ Update attributes of object """
        if len(args) >= 1:
            self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
                if len(args) >= 3:
                    self.x = args[2]
                    if len(args) == 4:
                        self.y = args[3]
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs[key]
                if key == 'size':
                    self.size = kwargs[key]
                if key == 'x':
                    self.x = kwargs[key]
                if key == 'y':
                    self.y = kwargs[key]
        super().__init__(self.size, self.size, self.x, self.y, self.id)

    def to_dictionary(self):
        """ Dictionary Representation of object """
        obj_dict = {}
        obj_dict['id'] = self.id
        obj_dict['size'] = self.size
        obj_dict['x'] = self.x
        obj_dict['y'] = self.y
        return obj_dict
