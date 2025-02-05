#!/usr/bin/python3
"""Module that returns True if the object is an instance of a class
   that inherited (directly or indirectly)
   from the specified class ; otherwise False."""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        True if `obj` is an instance of a class that inherited from `a_class`,
              False otherwise.
    """
    return isinstance(obj, a_class) and not issubclass(type(obj), a_class)
