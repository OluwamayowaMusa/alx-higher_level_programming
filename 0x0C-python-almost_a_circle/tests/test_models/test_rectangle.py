#!/usr/bin/python3
""" Unittest for Rectangle class.

"""
import unittest
import sys
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ Test cases for Rectangle Class.

    """

    @classmethod
    def setUpClass(cls):
        """ Setup test Examples as class attributes """
        cls.r1 = Rectangle(1, 2)
        cls.r2 = Rectangle(1, 8, 3)
        cls.r3 = Rectangle(5, 6, 3, 4)
        cls.r4 = Rectangle(3, 2, 3, 5, 5)

    @staticmethod
    def create_test_file(obj):
        """ Create file for display test.

        Args:
            obj: Rectangle Obj
        """
        temp = sys.stdout
        with open('display_test', 'w', encoding='utf-8') as sys.stdout:
            obj.display()
        sys.stdout = temp

    @staticmethod
    def load_test_file():
        """ Load the test file for display test """
        with open('display_test', 'r', encoding='utf-8') as test_file:
            lines = test_file.readlines()
        return lines

    def test_rectangle(self):
        """ Test attributes of Rectangle Objects """
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r2.height, 8)
        self.assertEqual(self.r3.x, 3)
        self.assertEqual(self.r4.y, 5)
        self.assertEqual(self.r4.id, 5)

    def test_values(self):
        """ Test Values passed to Rectangle class """
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

    def test_area(self):
        """ Test the area method of Rectangle object """
        self.assertEqual(self.r1.area(), 2)
        self.assertEqual(self.r2.area(), 8)
        self.assertEqual(self.r3.area(), 30)
        self.assertEqual(self.r4.area(), 6)

    def test_str(self):
        """ Test string Representation of Rectangle Object """
        self.assertEqual(str(self.r1), "[Rectangle] (3) 0/0 - 1/2")
        self.assertEqual(str(self.r2), "[Rectangle] (4) 3/0 - 1/8")

    def test_display(self):
        """ Test the display method of Rectangle Object """
        self.create_test_file(self.r1)
        lines = self.load_test_file()
        self.assertEqual(len(lines), self.r1.height)
        self.assertEqual(len(lines[-1]) - 1, self.r1.width)
        self.create_test_file(self.r2)
        lines = self.load_test_file()
        self.assertEqual(len(lines), self.r2.height)
        self.assertEqual(len(lines[-1]) - 1, self.r2.width + self.r2.x)
        self.create_test_file(self.r3)
        lines = self.load_test_file()
        self.assertEqual(len(lines), self.r3.height + self.r3.y)
        self.assertEqual(len(lines[-1]) - 1, self.r3.width + self.r3.x)

    def test_to_dictionary(self):
        """ Test method to_dictionary of Rectangle Object """
        self.assertDictEqual(self.r1.to_dictionary(),
                             {'id': 3, 'x': 0, 'y': 0, 'width': 1,
                             'height': 2})
        self.assertDictEqual(self.r2.to_dictionary(),
                             {'id': 4, 'x': 3, 'y': 0, 'width': 1,
                             'height': 8})

    def test_update(self):
        """ Test method update of Rectangle Object """
        self.r1.update()
        self.assertEqual(self.r1.id, 3)
        self.r1.update(50)
        self.assertEqual(self.r1.id, 50)
        self.r1.update(50, 5)
        self.assertEqual(self.r1.width, 5)
        self.r1.update(50, 5, 3)
        self.assertEqual(self.r1.height, 3)
        self.r1.update(50, 5, 3, 8)
        self.assertEqual(self.r1.x, 8)
        self.r1.update(50, 5, 3, 8, 9)
        self.assertEqual(self.r1.y, 9)
        self.r2.update(**{'id': 75})
        self.assertEqual(self.r2.id, 75)
        self.r2.update(**{'id': 75, 'width': 3})
        self.assertEqual(self.r2.width, 3)
        self.r2.update(**{'id': 75, 'width': 3, 'height': 6})
        self.assertEqual(self.r2.height, 6)
        self.r2.update(**{'id': 75, 'width': 3, 'height': 6, 'x': 5})
        self.assertEqual(self.r2.x, 5)
        self.r2.update(**{'id': 75, 'width': 3, 'height': 6, 'x': 5, 'y': 7})
        self.assertEqual(self.r2.y, 7)

    def test_create(self):
        """ Test method create for Rectangle Object """
        obj = Rectangle.create(**{'id': 23})
        self.assertEqual(obj.id, 23)
        obj = Rectangle.create(**{'id': 23, 'width': 4})
        self.assertEqual(obj.width, 4)
        obj = Rectangle.create(**{'id': 23, 'width': 4, 'height': 3})
        self.assertEqual(obj.height, 3)
        obj = Rectangle.create(**{'id': 23, 'width': 4, 'height': 3, 'x': 3})
        self.assertEqual(obj.x, 3)
        obj = Rectangle.create(**{'id': 23, 'width': 4, 'height': 3,
                                  'x': 3, 'y': 5})
        self.assertEqual(obj.y, 5)

    def test_file_methods(self):
        """ Test method save_to_file and load_from_file for Rectangle Object.
        """
        list_obj = Rectangle.load_from_file()
        self.assertListEqual(list_obj, [])
        Rectangle.save_to_file(None)
        list_obj = Rectangle.load_from_file()
        self.assertListEqual(list_obj, [])
        Rectangle.save_to_file([Rectangle(1, 2)])
        list_obj = Rectangle.load_from_file()
        self.assertEqual(list_obj[0].width, 1)

    @classmethod
    def tearDownClass(cls):
        """ Deletes test Examples """
        del cls.r1
        del cls.r2
        del cls.r3
