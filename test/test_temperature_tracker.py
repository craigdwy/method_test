#!/usr/bin/env python

# Python module
import random
import unittest

# Package module
from method_test import temperature_tracker
"""Unit test for the temperature_tracker.TempTracker"""


class TestTemperatureTracker(unittest.TestCase):

    def test_insert(self):

        temperature_object = temperature_tracker.TempTracker()
        # successful insert
        # test 5 random number in the allowed range
        test_input = random.sample(
            range(
                temperature_tracker.TempTracker.MIN_ALLOWED_TEMPERATURE,
                temperature_tracker.TempTracker.MAX_ALLOWED_TEMPERATURE
            ), 5
        )
        # test edge cases
        test_input.extend(
            [
                temperature_tracker.TempTracker.MIN_ALLOWED_TEMPERATURE,
                temperature_tracker.TempTracker.MAX_ALLOWED_TEMPERATURE
            ]
        )

        for i in test_input:
            self.assertTrue(temperature_object.insert(input_temperature=i))

        # un-successful insert
        bad_values = [-1.1, -110.1, 120]
        for i in bad_values:
            self.assertFalse(temperature_object.insert(input_temperature=i))

    def test_min_max(self):

        test_input = [15, 7, 57, 3, 109]
        temperature_object = temperature_tracker.TempTracker()
        for i in test_input:
            temperature_object.insert(i)

        self.assertEqual(temperature_object.get_max(), 109)
        self.assertEqual(temperature_object.get_min(), 3)

    def test_mean(self):
        test_input = [15, 7, 57, 3, 109]
        temperature_object = temperature_tracker.TempTracker()
        # Test with no input
        self.assertEqual(temperature_object.get_mean(), 0)
        for i in test_input:
            temperature_object.insert(i)
        self.assertEqual(temperature_object.get_mean(), 38.2)
        self.assertEqual(temperature_object.calculate_mean(), 38.2)  # Alternate python 2.7 method

    def test_bad_input(self):
        temperature_object = temperature_tracker.TempTracker()
        with self.assertRaises(TypeError):
            temperature_object.insert([])


if __name__ == '__main__':
    unittest.main()
