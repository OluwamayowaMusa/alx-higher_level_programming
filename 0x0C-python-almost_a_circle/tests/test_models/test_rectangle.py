#!/usr/bin/python3
""" Unittest for Rectangle class.

"""

import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ Test cases for Rectangle class """

    def setUp(self):
        """ Setup the test example """
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(7, 6, 0, 0, 13)

    def test_id(self):
        """ Test id """
        self.assertEqual(self.r1.id, 14)
        self.assertEqual(self.r2.id, 13)

    def test_values(self):
        """ Test for exception """
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(TypeError, Rectangle, 10, 2, [])
        self.assertRaises(ValueError, Rectangle, 10, 2, 2, -1)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

    def test_area(self):
        """ Test method area """
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 42)

    def test_str(self):
        """ Test string Representation of object """
        self.assertEqual(str(self.r1), "[Rectangle] (19) 0/0 - 10/2")
        self.assertEqual(str(self.r2), "[Rectangle] (13) 0/0 - 7/6")

    def test_create(self):
        """ Test method create """
        obj = Rectangle.create(**{'id': 89})
        self.assertEqual(obj.id, 89)
        self.assertEqual(type(obj).__name__, "Rectangle")
        obj = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(obj.width, 1)
        obj = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(obj.area(), 2)
        obj = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(obj.x, 3)
        obj = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(obj.y, 4)

    def test_save_to_file(self):
        """ Test method save_to_file """
        self.assertEqual(Rectangle.save_to_file(None), None)
        self.assertEqual(Rectangle.save_to_file([]), None)
        self.assertEqual(Rectangle.save_to_file([Rectangle(1, 5)]), None)

    def test_load_from_file(self):
        """ Test method load_from_file """
        self.assertEqual(Rectangle.load_from_file()[0].width, 1)

    def test_update(self):
        """ Test update method """
        self.r1.update(89)
        self.r2.update(id=15)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r2.id, 15)

    def test_to_dictionary(self):
        """ Test method to_dictionary """
        r2_dict = self.r2.to_dictionary()
        self.assertEqual(type(r2_dict), dict)
        self.assertDictEqual(r2_dict, {'id': 13, 'x': 0, 'y': 0, 'width': 7,
                             'height': 6})

    def tearDown(self):
        """ Dispose created object """
        del self.r1
        del self.r2
