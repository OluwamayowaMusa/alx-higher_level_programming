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
        self.s2 = Square(1, 2, 3, 4)

    def test_attributes(self):
        """ Test attributes of object """
        self.assertEqual(self.s1.area(), 25)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s1.id, 23)
        self.assertEqual(self.s2.id, 4)

    def test_values(self):
        """ Test arguments passed """
        self.assertRaises(TypeError, Square, {})
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 5, -2)
        self.assertRaises(TypeError, Square, 5, [])
        self.assertRaises(TypeError, Square, 1, 2, "3")
        self.assertRaises(ValueError, Square, 5, 1, -7)

    def test_str_(self):
        """ Test method str """
        self.assertEqual(str(self.s2), "[Square] (4) 2/3 - 1")

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
        self.assertDictEqual(s1_dict, {'id': 34, 'size': 5, 'x': 0, 'y': 0})

    def test_create(self):
        """ Test method create """
        obj = Square.create(**{'id': 89})
        self.assertEqual(obj.id, 89)
        obj = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(obj.area(), 1)
        obj = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(obj.x, 2)
        obj = Square.create(**{'id': 89, 'size' : 1, 'x': 2, 'y': 3})
        self.assertEqual(obj.y, 3)

    def test_save_to_file(self):
        """ Test save_to_file method """
        self.assertEqual(Square.save_to_file(None), None)
        self.assertEqual(Square.save_to_file([]), None)
        self.assertEqual(Square.save_to_file([Square(1)]), None)

    def test_load_from_file(self):
        """ Test load_from_file """
        self.assertEqual(Square.load_from_file()[0].size, 1)

    def tearDown(self):
        """ Dispose Object """
        del self.s1
