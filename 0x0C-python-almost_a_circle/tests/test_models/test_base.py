#!/usr/bin/python3
""" Unittest for the base class.

"""

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ Test cases for the Base class.

    """

    def setUp(self):
        """ Setup the test case """
        self.b1 = Base()
        self.b2 = Base(12)
        self.b3 = Base()

    def test_id(self):
        """ Test id values of instances of Base class """
        self.assertEqual(self.b1.id, 3)
        self.assertEqual(self.b2.id, 12)
        self.assertEqual(self.b3.id, 4)


    def test_from_json_string(self):
        """ Test method from_json_string """
        self.assertListEqual(Base.from_json_string(None), [])
        self.assertListEqual(Base.from_json_string("[]"), [])
        self.assertListEqual(Base.from_json_string('[{"id": 12}]'), [{"id": 12}])

    def tearDown(self):
        """ Dispose Created Object """
        del self.b1
        del self.b2
        del self.b3
