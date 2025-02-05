#!/usr/bin/python3
"""Module for geometric shape validation and area calculations.

This module contains the BaseGeometry class, which provides methods
for validating integer inputs and calculating geometric shape areas.
"""


class BaseGeometry:
    """Empty class for geometric uses"""

    def area(self):
        """Function calculating area of geometric shapes
           Raises exception if the area is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if int is 0 or greater ergo a valid input
           Args:
                name (str): The name of the parameter (string).
                value (int): The value to be validated (integer).
           Raises:
                  TypeError: If the value is not an integer.
                  ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
