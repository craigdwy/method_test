#!/usr/bin/env python

# Python module
import unittest

# Package module
from method_test import flatten_array
"""Unit test for the flatten_array.flatten_array"""


class TestFlattenArray(unittest.TestCase):

    def test_input(self):
        self.assertEqual(
            flatten_array.flatten_array([[1, 2, [3]], 4]), [1, 2, 3, 4]
        )
        self.assertEqual(
            flatten_array.flatten_array([["a", "b", [3]], " ", [[[[None], [4]], 5]]]), [3, 4, 5]
        )
        self.assertEqual(
            flatten_array.flatten_array([]), []
        )

    def test_bad_input(self):
        with self.assertRaises(TypeError):
            flatten_array.flatten_array((1, (2, 3)))


if __name__ == '__main__':
    unittest.main()
