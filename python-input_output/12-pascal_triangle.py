#!/usr/bin/python3
"""A module to generate Pascal's triangle."""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of size n.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists containing Pascal's triangle values.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the last row
        new_row = [1]

        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j + 1])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
