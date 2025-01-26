#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.

The matrix_divided function ensures input matrix is properly formatted,
checks for valid inputs, and returns a new matrix where each element is divided
by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix (list of lists) of integers or floats.
        div (int or float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if rows of the matrix are not the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is 0.

    Returns:
        list of lists: A new matrix with all elements divided by div,
                       rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) == 0 or not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
