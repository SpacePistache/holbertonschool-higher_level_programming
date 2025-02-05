#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class; False otherwise

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise
    """
    if type(obj) is a_class:
        return True
    return False
