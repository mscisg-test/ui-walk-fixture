"""Toy heat index helper for the UI walk fixture — nothing real."""


def heat_index_f(temp_f, relative_humidity_pct):
    """Approximate heat index in Fahrenheit (Rothfusz regression).

    Only valid for temp_f >= 80 and relative_humidity_pct in [0, 100];
    below that threshold the regression isn't a good fit, so callers
    get the raw air temperature back instead of a misleading number.
    """
    if not 0 <= relative_humidity_pct <= 100:
        raise ValueError("relative_humidity_pct must be in [0, 100]")

    if temp_f < 80:
        return temp_f

    t, r = temp_f, relative_humidity_pct
    return (
        -42.379
        + 2.04901523 * t
        + 10.14333127 * r
        - 0.22475541 * t * r
        - 0.00683783 * t * t
        - 0.05481717 * r * r
        + 0.00122874 * t * t * r
        + 0.00085282 * t * r * r
        - 0.00000199 * t * t * r * r
    )
