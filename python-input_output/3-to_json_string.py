#!/usr/bin/python3
"""A module that returns the JSON representation of an object."""


import json


def to_json_string(my_obj):
    """A function that returns JSON rep of a string.

       Args:
            my_obj: what is going to be converted.

       Return:
              String in JSON format.

    """

    return json.dumps(my_obj)
