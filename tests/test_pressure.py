"""Tests for the toy barometric pressure helpers."""

import sys
import unittest

sys.path.insert(0, "src")

from pressure import SEA_LEVEL_PA, altitude_from_pressure, pressure_from_altitude


class TestAltitudeFromPressure(unittest.TestCase):
    def test_sea_level_pressure_is_zero_altitude(self):
        self.assertAlmostEqual(altitude_from_pressure(SEA_LEVEL_PA), 0, places=3)

    def test_lower_pressure_means_higher_altitude(self):
        self.assertGreater(altitude_from_pressure(90000), altitude_from_pressure(100000))

    def test_round_trip(self):
        altitude = altitude_from_pressure(95000)
        self.assertAlmostEqual(pressure_from_altitude(altitude), 95000, places=3)


if __name__ == "__main__":
    unittest.main()
