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

    def to_json(self):
        """ Retrieves dictionary representaion of object """
        return self.__dict__
