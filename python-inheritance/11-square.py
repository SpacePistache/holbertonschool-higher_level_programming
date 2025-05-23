#!/usr/bin/python3
"""Module for geometric shape validation and area calculations.

This module contains the BaseGeometry class, which provides methods
for validating integer inputs and calculating geometric shape areas.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle, has 4 equal sides"""

    def __init__(self, size):
        """Initialize Square instance

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
