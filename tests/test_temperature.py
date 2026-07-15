"""Tests for the toy temperature helpers."""

import sys
import unittest

sys.path.insert(0, "src")

from temperature import c_to_f, clamp, f_to_c


class TestConversions(unittest.TestCase):
    def test_boiling_point(self):
        self.assertEqual(c_to_f(100), 212)

    def test_freezing_point(self):
        self.assertEqual(f_to_c(32), 0)

    def test_round_trip(self):
        self.assertAlmostEqual(f_to_c(c_to_f(37.5)), 37.5)


class TestClamp(unittest.TestCase):
    def test_inside_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_below_range(self):
        self.assertEqual(clamp(-3, 0, 10), 0)

    def test_invalid_range_raises(self):
        with self.assertRaises(ValueError):
            clamp(1, 10, 0)


if __name__ == "__main__":
    unittest.main()
