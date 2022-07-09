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
        self.r2 = Rectangle(7, 6, 0, 0, 12)

    def test_id(self):
        """ Test id """
        self.assertEqual(self.r1.id, 2)
        self.assertEqual(self.r2.id, 12)

    def test_values(self):
        """ Test for exception """
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(TypeError, Rectangle, 10, 2, [])
        self.assertRaises(ValueError, Rectangle, 10, 2, 2, -1)

    def test_area(self):
        """ Test method area """
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 42)
