#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class; False otherwise.

    Function checks if object is exact instance of the class `a_class`.
    Does not consider objects that are instances of subclasses of `a_class`.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if `obj` is an instance of `a_class`, False otherwise.
    """
    return type(obj) is a_class
