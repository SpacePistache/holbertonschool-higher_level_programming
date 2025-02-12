#!/usr/bin/python3
"""A module that writes an Object to a file using JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """A function that allows to do this

        Args:
            my_obj: what will be written
            filename: the destination of the object

        Return:
            None
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
