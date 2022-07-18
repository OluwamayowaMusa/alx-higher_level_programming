#!/usr/bin/python3
""" Unittest for The Base Class.

"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


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

    def test_to_json_string(self):
        """ Test method to_json_string """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        """ Test method from_json_string """
        self.assertListEqual(Base.from_json_string(None), [])
        self.assertListEqual(Base.from_json_string("[]"), [])
        self.assertListEqual(Base.from_json_string('[{"id": 8}]'), [{"id": 8}])

    @classmethod
    def tearDownClass(cls):
        """ Delete test examples """
        del cls.b1
        del cls.b2
        del cls.b3
