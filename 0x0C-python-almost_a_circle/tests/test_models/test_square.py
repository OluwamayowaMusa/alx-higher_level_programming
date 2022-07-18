#!/usr/bin/python3
""" Unittest for the Square class.

"""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """ Test cases for Square class.

    """

    @classmethod
    def setUpClass(cls):
        """ Setup Test examples """
        cls.s1 = Square(1)
        cls.s2 = Square(1, 2)
        cls.s3 = Square(1, 2, 3)
        cls.s4 = Square(1, 2, 3, 4)

    def test_attributes(self):
        """ Test attributes of Square object """
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s3.y, 3)
        self.assertEqual(self.s4.id, 4)

    def test_values(self):
        """ Test values passed to Square class """
        self.assertRaises(TypeError, Square, "1")
        self.assertRaises(TypeError, Square, 1, "2")
        self.assertRaises(TypeError, Square, 1, 2, "3")
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 1, 2, -3)
        self.assertRaises(ValueError, Square, 0)

    def test_str(self):
        """ Test string representaion of Square Object """
        self.assertEqual(str(self.s1), "[Square] (13) 0/0 - 1")
        self.assertEqual(str(self.s2), "[Square] (14) 2/0 - 1")

    @classmethod
    def tearDownClass(cls):
        """ Delete Test Examples """
        del cls.s1
        del cls.s2
        del cls.s3
