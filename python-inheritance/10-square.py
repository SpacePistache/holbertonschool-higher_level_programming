#!/usr/bin/python3
"""Module for geometric shape validation and area calculations.

This module contains the BaseGeometry class, which provides methods
for validating integer inputs and calculating geometric shape areas.
"""
Rectangle = __import__('8-rectangle').Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle, has for equal sides"""

    def __init__(self, size):
        """Initialize Square instance

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
