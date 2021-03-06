#!/usr/bin/python3
""" Defines Base class.

"""
import json
import os
import turtle


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

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw the objects.

        Args:
            list_rectangles (list): List of Object Rectangle
            list_squares (list): List of Object Square
        """
        s = turtle.getscreen()
        t = turtle.getturtle()
        for obj_rect in list_rectangles:
            t.penup()
            t.goto(obj_rect.x, obj_rect.y)
            t.pendown()
            t.color('red', 'black')
            t.begin_fill()
            for i in range(2):
                t.fd(obj_rect.width)
                t.rt(90)
                t.fd(obj_rect.height)
                t.rt(90)
            t.end_fill()

        for obj_squ in list_squares:
            t.penup()
            t.goto(obj_squ.x, obj_squ.y)
            t.pendown()
            t.color('blue', 'green')
            t.begin_fill()
            t.rt(45)
            t.circle(obj_squ.size, steps=4)
            t.lt(45)
            t.end_fill()

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write the JSON string representation to a file.

        Args:
            list_objs (list): List of objects to write to file.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(cls.to_json_string([]))
            return
        list_dict = []
        for obj in list_objs:
            list_dict.append(obj.to_dictionary())
        json_string = cls.to_json_string(list_dict)
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
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save the object attributes in CSV format.

        Args:
            list_objs (list): List of class instances
        """
        obj_csv = []
        for obj in list_objs:
            obj_dict = obj.to_dictionary()
            temp_list = []
            for key, value in obj_dict.items():
                if key == 'id':
                    temp_list.insert(0, str(value))
                if cls.__name__ == 'Rectangle':
                    if key == 'width':
                        temp_list.insert(1, str(value))
                    elif key == 'height':
                        temp_list.insert(2, str(value))
                    elif key == 'x':
                        temp_list.insert(3, str(value))
                    elif key == 'y':
                        temp_list.insert(4, str(value))
                elif cls.__name__ == 'Square':
                    if key == 'size':
                        temp_list.insert(1, str(value))
                    elif key == 'x':
                        temp_list.insert(2, str(value))
                    elif key == 'y':
                        temp_list.insert(3, str(value))
            temp_str = ','.join(temp_list) + '\n'
            obj_csv.append(temp_str)
        if len(list_objs) != 0:
            filename = cls.__name__ + ".csv"
            with open(filename, 'w', encoding='utf-8') as f:
                f.writelines(obj_csv)

    @classmethod
    def load_from_file_csv(cls):
        """ Load object attributes """
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []
        list_objs = []
        with open(filename, 'r', encoding='utf-8') as f:
            list_attr = f.readlines()
        for attrs in list_attr:
            temp = attrs.split(',')
            temp_list = []
            for index, attr in enumerate(temp):
                if index != len(temp) - 1:
                    temp_list.append(int(attr))
                else:
                    temp_list.append(int(attr[:-1]))
            obj = cls(1, 1)
            obj.update(*temp_list)
            list_objs.append(obj)

        return list_objs
