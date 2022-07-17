#!/usr/bin/python3

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ Test cases for the Base Class """

    def test_id(self):
        """ Test the id of base object """
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
