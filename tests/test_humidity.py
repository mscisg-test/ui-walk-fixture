"""Tests for the toy humidity helpers."""

import sys
import unittest

sys.path.insert(0, "src")

from humidity import dew_point_c


class TestDewPoint(unittest.TestCase):
    def test_saturated_air_equals_air_temp(self):
        # At 100% relative humidity, dew point == air temperature.
        self.assertAlmostEqual(dew_point_c(20, 1.0), 20, places=6)

    def test_drier_air_has_lower_dew_point(self):
        self.assertLess(dew_point_c(20, 0.4), dew_point_c(20, 0.8))

    def test_rejects_out_of_range_humidity(self):
        with self.assertRaises(ValueError):
            dew_point_c(20, 0)

        with self.assertRaises(ValueError):
            dew_point_c(20, 1.2)


if __name__ == "__main__":
    unittest.main()
