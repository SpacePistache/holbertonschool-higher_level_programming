#!/usr/bin/python3
"""A module returning a dictionary of an object's attributes."""


def class_to_json(obj):
    """Function returning aforementioned elements
        Args:
            obj: Class instance.

        Return:
            A dictionary of obj's attributes.
    """
    return obj.__dict__
