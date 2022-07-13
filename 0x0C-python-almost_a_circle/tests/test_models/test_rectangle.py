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
        self.assertEqual(self.r1.id, 9)
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
        self.assertEqual(str(self.r1), "[Rectangle] (10) 0/0 - 10/2")
        self.assertEqual(str(self.r2), "[Rectangle] (13) 0/0 - 7/6")

    def test_display(self):
        """ Test method display """
        self.assertEqual(self.r1.display(), None)
        self.assertEqual(self.r2.display(), None)

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
