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

    def test_to_dictionary(self):
        """ Test method to_dictionary of Square object """
        self.assertDictEqual(self.s1.to_dictionary(),
                            {'id': 13, 'x': 0, 'y': 0, 'size': 1})

    def test_update(self):
        """ Test method update of Square Object """
        self.s1.update()
        self.assertEqual(self.s1.id, 13)
        self.s1.update(50)
        self.assertEqual(self.s1.id, 50)
        self.s1.update(50, 5)
        self.assertEqual(self.s1.size, 5)
        self.s1.update(50, 5, 3)
        self.assertEqual(self.s1.x, 3)
        self.s1.update(50, 5, 3, 9)
        self.assertEqual(self.s1.y, 9)
        self.s2.update(**{'id': 75})
        self.assertEqual(self.s2.id, 75)
        self.s2.update(**{'id': 75, 'size': 3})
        self.assertEqual(self.s2.size, 3)
        self.s2.update(**{'id': 75, 'size': 3, 'x': 6})
        self.assertEqual(self.s2.x, 6)
        self.s2.update(**{'id': 75, 'size': 3, 'x': 6, 'y': 5})
        self.assertEqual(self.s2.y, 5)

    def test_create(self):
        """ Test method create for Square Object """
        obj = Square.create(**{'id': 23})
        self.assertEqual(obj.id, 23)
        obj = Square.create(**{'id': 23, 'size': 4})
        self.assertEqual(obj.size, 4)
        obj = Square.create(**{'id': 23, 'size': 4, 'x': 3})
        self.assertEqual(obj.x, 3)
        obj = Square.create(**{'id': 23, 'size': 4, 'x': 3, 'y': 3})
        self.assertEqual(obj.y, 3)

    @classmethod
    def tearDownClass(cls):
        """ Delete Test Examples """
        del cls.s1
        del cls.s2
        del cls.s3
