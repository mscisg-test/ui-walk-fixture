"""Toy barometric pressure helpers for the UI walk fixture — nothing real."""

SEA_LEVEL_PA = 101325
LAPSE_EXPONENT = 5.255


def altitude_from_pressure(pressure_pa, sea_level_pa=SEA_LEVEL_PA):
    """Approximate altitude in meters from barometric pressure in pascals."""
    ratio = pressure_pa / sea_level_pa
    return 44330 * (1 - ratio ** (1 / LAPSE_EXPONENT))


def pressure_from_altitude(altitude_m, sea_level_pa=SEA_LEVEL_PA):
    """Inverse of altitude_from_pressure."""
    return sea_level_pa * (1 - altitude_m / 44330) ** LAPSE_EXPONENT
