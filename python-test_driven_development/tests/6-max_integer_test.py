#!/usr/bin/python3
"""Unittest for max_integer([..])

This module contains comprehensive unit tests for the max_integer function
to ensure it correctly finds the maximum integer in a list under various conditions.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a standard list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_numbers(self):
        """Test with list containing negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-10, 0, 10]), 10)
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

    def test_single_element(self):
        """Test with a list containing only one element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_duplicate_max(self):
        """Test with duplicate maximum values"""
        self.assertEqual(max_integer([5, 5, 5]), 5)
        self.assertEqual(max_integer([1, 5, 5, 2]), 5)

    def test_zero_values(self):
        """Test with zero values"""
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)
        self.assertEqual(max_integer([-1000000, -999999, -1000001]), -999999)

if __name__ == '__main__':
    unittest.main()