#!/usr/bin/python3
"""A module that converts a JSON string into a Python data structure"""


import json


def from_json_string(my_str):
    """A functions that converts JSON string into a Python structure

        Args:
            my_str: What gets parsed and converted.
        Returns:
            The Python data structure.
    """
    return json.loads(my_str)
