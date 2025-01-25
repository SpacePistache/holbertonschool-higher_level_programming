#!/usr/bin/python3
"""
This module provides a function to add two integers.

The function takes two arguments and returns their sum as an integer.
Inputs either integers/floats and raises exceptions for invalid inputs.
"""


def add_integer(a, b=98):
    """
    This function adds two integers (or floats).
    If'a' or 'b' is a float, will be cast to an int before adding.

    Parameters:
    - a: The first number (integer or float).
    - b: The second number (integer or float, defaults to 98).

    Returns:
    - The sum of the two numbers as an integer.

    Raises:
    - TypeError: If either 'a' or 'b' is not an integer or float.
    - ValueError: If either 'a' or 'b' is NaN.
    - OverflowError: If either 'a' or 'b' causes an overflow when converted.
    """
    import math

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for NaN values
    if isinstance(a, float) and math.isnan(a):
        raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float) and math.isnan(b):
        raise ValueError("cannot convert float NaN to integer")

    try:
        a = int(a)
    except OverflowError:
        raise OverflowError("a is too large to be converted to an integer")

    try:
        b = int(b)
    except OverflowError:
        raise OverflowError("b is too large to be converted to an integer")

    return a + b
