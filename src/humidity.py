"""Toy humidity helpers for the UI walk fixture — nothing real."""

import math


def dew_point_c(temp_c, relative_humidity):
    """Approximate dew point (Celsius) via the Magnus formula.

    `relative_humidity` is a fraction in (0, 1] — pass 0.65 for 65% RH.
    Out-of-range values raise ValueError.
    """
    if not 0 < relative_humidity <= 1:
        raise ValueError("relative_humidity must be in (0, 1]")

    a, b = 17.62, 243.12
    gamma = (a * temp_c) / (b + temp_c) + math.log(relative_humidity)
    return (b * gamma) / (a - gamma)
