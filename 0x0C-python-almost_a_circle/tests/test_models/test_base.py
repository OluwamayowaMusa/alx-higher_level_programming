#!/usr/bin/python3
""" Unittest for The Base Class.

"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """  Test cases for the Base class.

    """

    @classmethod
    def setUpClass(cls):
        """ Setup test examples as class attributes """
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base(19)

    def test_id(self):
        """ Test the id of Base Objects """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 19)
