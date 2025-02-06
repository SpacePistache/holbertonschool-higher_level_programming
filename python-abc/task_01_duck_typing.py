#!/usr/bin/python3
"""This module uses abstract classes and duck types applied to shapes."""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """This a parent class for Shapes."""
    @abstractmethod
    def area(self):
        """Calculate and returns area of shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates and returns the perimeter of the shape."""
        pass


class Circle(Shape):
    """A circle boi, child of Shape class."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates and returns the area of Circle boi."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculates and returns perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A rectangle lad, four sides."""
    def __init__(self, width, height):
        """Initialize rectangle lad, with width and height parameters."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates the area of our Rectangle lad"""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of Rectangliest of Rectangles"""
        return 2 * (self.width + self.height)

def Shape_info(shape):
    """Area and perimeter of Rectangle and Circle."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
