#!/usr/bin/python3
""" Unittest for Rectangle class.

"""
import unittest
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

    @classmethod
    def tearDownClass(cls):
        """ Deletes test Examples """
        del cls.r1
        del cls.r2
        del cls.r3
