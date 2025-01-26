#!/usr/bin/python3
"""
This module provides a simple function to print a person's full name.

It includes a function say_my_name that takes a first name and an optional
last name, and prints the full name. The function includes type checking
to ensure both names are strings.
"""


def say_my_name(first_name, last_name=""):
    """
    Print the full name of a person.

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.

    Prints:
        The full name in the format "My name is <first_name> <last_name>"
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}".rstrip())
