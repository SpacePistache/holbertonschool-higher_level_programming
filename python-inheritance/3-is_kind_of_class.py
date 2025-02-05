#!/usr/bin/python3
"""Module checking if obj is instance of class or inherited class."""


def is_kind_of_class(obj, a_class):
    """
    Returns 'True' if obj instance of class/instance inherited.

    Args:
        obj: (object) being checked.
        a_class: The class being compared.

    Returns: True if so, false if not.

    """
    return isinstance(obj, a_class)
