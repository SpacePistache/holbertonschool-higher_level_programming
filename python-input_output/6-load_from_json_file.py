#!/usr/bin/python3
"""A module that writes an Object to a file using JSON representation"""


import json


def load_from_json_file(filename):
    """A function that allows to do this

        Args:
            my_obj: what will be written
            filename: the destination of the object

        Return:
            The Python object stored in the file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        json.load(file)
