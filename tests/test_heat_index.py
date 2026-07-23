"""Tests for the toy heat index helper."""

import sys
import unittest

sys.path.insert(0, "src")

from heat_index import heat_index_f


class TestHeatIndex(unittest.TestCase):
    def test_below_threshold_returns_air_temp(self):
        self.assertEqual(heat_index_f(75, 50), 75)

    def test_known_value(self):
        # 90F at 50% RH is a commonly cited reference point (~94.6F).
        self.assertAlmostEqual(heat_index_f(90, 50), 94.6, delta=0.5)

    def test_higher_humidity_increases_index(self):
        self.assertGreater(heat_index_f(90, 80), heat_index_f(90, 40))

    def test_rejects_out_of_range_humidity(self):
        with self.assertRaises(ValueError):
            heat_index_f(90, 150)


if __name__ == "__main__":
    unittest.main()
