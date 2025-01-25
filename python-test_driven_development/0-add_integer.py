def add_integer(a, b=98):
    """
    This function adds two integers (or floats).
    If'a' or 'b' is float, it will be cast to an integer before adding.

    Parameters:
    - a: The first number (integer or float).
    - b: The second number (integer or float, defaults to 98).

    Returns:
    - The sum of the two numbers as an integer.

    Raises:
    - TypeError: If either 'a' or 'b' is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError(
            "a must be an integer"
        )
    if not isinstance(b, (int, float)):
        raise TypeError(
            "b must be an integer"
        )

    return int(a) + int(b)
