#!/usr/bin/python3
""" Unittest for the base class.

"""

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ Test cases for the Base class.

    """

    def setUp(self):
        """ Setup test examples """
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(89)

    def test_id(self):
        """ Test id of base Object """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 89)

