#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.

The matrix_divided function takes a matrix (list of lists) and a divisor,
then returns a new matrix with all elements divided by the divisor,
rounded to two decimal places. It includes comprehensive input validation
to ensure the matrix and divisor meet specific criteria.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The number to divide all matrix elements by.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   if rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list: A new matrix with elements divided by div and rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
