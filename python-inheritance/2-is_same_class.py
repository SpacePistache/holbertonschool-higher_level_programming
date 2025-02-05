#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    This function compares the object to the class and returns True if the
    object is an exact instance of the specified class, otherwise it returns
    False. This does not consider inheritance or subclasses.

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
