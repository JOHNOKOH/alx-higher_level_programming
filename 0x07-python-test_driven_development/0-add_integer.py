#!/usr/bin/python3
<<<<<<< HEAD
# 0-dd_integer.py
"""An integer addition function is defined."""

def add_integer(a, b=98):
    """The addition integer of a and b is returned.
=======
# 0-add_integer.py
"""An integer addition function is defined."""


def add_integer(a, b=98):
    """The integer addition of a and b is returned.
>>>>>>> ccb1e7d633d6fd472e2effd67893e19ad6446e4b

    Float arguments are typecasted to ints before addition is performed.

    Note:
<<<<<<< HEAD
    a and b must be integers or floats, otherwise raise a TypeError
=======
        a and b must be integers or floats, otherwise raise a TypeError
>>>>>>> ccb1e7d633d6fd472e2effd67893e19ad6446e4b
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
