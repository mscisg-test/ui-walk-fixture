"""Toy temperature helpers for the UI walk fixture — nothing real."""


def c_to_f(celsius):
    """Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    """Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def clamp(value, low, high):
    """Clamp value into [low, high]."""
    if low > high:
        raise ValueError("low must not exceed high")
    return max(low, min(high, value))


def wind_chill(temp_f, wind_mph):
    """NWS wind chill. WIP: domain validation still undecided (see issue #6)."""
    factor = wind_mph ** 0.16
    return 35.74 + 0.6215 * temp_f - 35.75 * factor + 0.4275 * temp_f * factor
