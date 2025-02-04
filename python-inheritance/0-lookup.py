#!/usr/bin/python3
def lookup(obj):

    """Returns a list of available attributes and methods of an object."""
    return list(obj.__dict__.keys()) if hasattr(obj, '__dict__') else []
