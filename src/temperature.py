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
