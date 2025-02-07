#!/usr/bin/python3
"""Module for geometric shape validation and area calculations.

This module contains the BaseGeometry class, which provides methods
for validating integer inputs and calculating geometric shape areas.
"""


class BaseGeometry:
    """A class for geometric uses"""

    def area(self):
        """Raises an exception indicating the area method is not implemented.
    This method is meant to be implemented in subclasses of BaseGeometry.
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


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize Rectangle instance.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of the rectangle

        Returns:
            str: String in the format [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


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
    
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
