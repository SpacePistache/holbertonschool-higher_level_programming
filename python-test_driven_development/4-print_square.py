#!/usr/bin/python3
"""
This module provides a function to print a square made of '#' characters.

The print_square function allows users to create a square of a specified size
using the '#' character, with comprehensive input validation to ensure
the size is a valid non-negative integer.
"""


def print_square(size):
    """
    Print a square of '#' characters with the given size.

    Args:
        size (int): The length and width of the square to be printed.

    Raises:
        TypeError: If size is not an integer or is a float less than 0.
        ValueError: If size is less than 0.

    Prints:
        A square of '#' characters with dimensions size x size.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        # Special check for float to match the specific requirement
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")

    # Check if size is non-negative
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
