#!/usr/bin/python3
""" Defines a class Student.

"""


class Student:
    """ Describes student.

    """

    def __init__(self, first_name, last_name, age):
        """ Initailizes the object.

        Args:
            first_name (str): First name of student
            last_name (str): Last name of student
            age (int): Age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves dictionary representaion of object.

        Args:
            attrs (list): List of attributes to return

        Returns:
            dictionary of attributes
        """
        if attrs is None:
            return self.__dict__
        attr_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                attr_dict[attr] = self.__dict__[attr]
        return attr_dict
