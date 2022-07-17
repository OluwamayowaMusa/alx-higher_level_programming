#!/usr/bin/python3
""" Unittest for the base class.

"""

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ Test cases for the Base class.

    """
    @classmethod
    def setUpClass(cls):
        """ Test Examples for test methods """
        print("Setup class")
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base(89)

    def test_id(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 89)

    @classmethod
    def tearDownClass(cls):
        """ Delete test examples """
        print("Tear down")
        del cls.b1
        del cls.b2
        del cls.b3
