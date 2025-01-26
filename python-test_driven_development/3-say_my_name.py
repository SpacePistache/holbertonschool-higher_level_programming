#!/usr/bin/python3
"""
This module provides a function to print a person's full name.

The say_my_name function allows users to print a full name by combining
a first name and an optional last name, with comprehensive input validation
to ensure both names are strings.
"""


def say_my_name(first_name=None, last_name=None):
    """
    Print the full name of a person.

    Args:
        first_name (str, optional): The first name of the person.
        last_name (str, optional): The last name of the person.

    Raises:
        TypeError: If no arguments provided or arguments are not strings.

    Prints:
        The full name in the format "My name is <first_name> <last_name>"
    """

    if first_name is None and last_name is None:
        raise TypeError("say_my_name() missing 1 required positional argument: 'first_name'")

    if last_name is None:
        last_name = ""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name}{' ' + last_name if last_name else ' '}")
