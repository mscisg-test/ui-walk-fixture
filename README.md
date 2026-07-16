# ui-walk-fixture

Throwaway test fixture for UI parity walks — nothing real

## Helpers

`src/temperature.py` provides:

- `c_to_f(celsius)` / `f_to_c(fahrenheit)` — conversions
- `clamp(value, low, high)` — clamps `value` into `[low, high]`; raises
  `ValueError` when `low > high` (inverted ranges are caller bugs, not
  silently reordered)

```python
>>> from temperature import clamp
>>> clamp(120, 0, 100)
100
```

Tests live in `tests/` and run via `python -m unittest discover -s tests`.
Co-author walk line (fixture).
