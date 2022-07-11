#!/usr/bin/python3
""" Defines Base class.

"""
import json
import os


class Base:
    """ A base class for all other classes.

    Attributes:
        __nb_objects (private-int): Number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the object.

        Args:
            id (int): Id of object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON represenataion of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries

        Returns:
            JSON string representation of args
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ List of JSON string representation.

        Args:
            json_string (str): JSON string representation

        Returns:
            List of the JSON string reprentation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write the JSON string representation to a file.

        Args:
            list_objs (list): List of objects to write to file.
        """
        list_dict = []
        for obj in list_objs:
            list_dict.append(obj.to_dictionary())
        json_string = cls.to_json_string(list_dict)
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance of the cls.

        Args:
            dictionary (dict): Dictionary of attibutes of class

        Returns:
            Instance of the class
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns list of instances """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as f:
            json_object = f.read()

        list_dict = cls.from_json_string(json_object)
        list_obj = []
        for attr in list_dict:
            list_obj.append(cls.create(**attr))

        return list_obj
