#!/usr/bin/python3
""" Unittest for Square class

"""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """ Test cases """

    def setUp(self):
        """ Setup test example """
        self.s1 = Square(5)

    def test_attributes(self):
        """ Test attributes of object """
        self.assertEqual(self.s1.area(), 25)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s1.id, 14)

    def test_values(self):
        """ Test arguments passed """
        self.assertRaises(TypeError, Square, {})
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 5, -2)
        self.assertRaises(TypeError, Square, 5, [])
        self.assertRaises(ValueError, Square, 5, 1, -7)

    def test_update(self):
        """ Test update method """
        self.s1.update(10)
        self.assertEqual(self.s1.id, 10)
        self.s1.update(size=4)
        self.assertEqual(self.s1.size, 4)

    def test_to_dictionary(self):
        """ Test method to_dictionary """
        s1_dict = self.s1.to_dictionary()
        self.assertEqual(type(s1_dict), dict)
        self.assertDictEqual(s1_dict, {'id': 15, 'size': 5, 'x': 0, 'y': 0})

    def tearDown(self):
        """ Dispose Object """
        del self.s1
