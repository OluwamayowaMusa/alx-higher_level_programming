#!/usr/bin/python3
""" Unittest for max_integer([...])
"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """ Methods max_integer function.

    """

    def test_max_integer(self):
        """ TestCase for right output """
        self.assertEqual(max([23, 2, 4, 5]), max_integer([23, 2, 4, 5]))
        self.assertEqual(max([1, 2, 8, 6, 3]), max_integer([1, 2, 8, 6, 3]))
        self.assertEqual(max([9, 99, 100]), max_integer([99, 99, 100]))
        self.assertEqual(None, max_integer([]))
        self.assertEqual(max([1]), max_integer([1]))
        self.assertEqual(max([-97, -5, -6, -1]),
                         max_integer([-97, -5, -6, -1]))
