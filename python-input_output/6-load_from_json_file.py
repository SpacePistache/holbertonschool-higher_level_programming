#!/usr/bin/python3
"""A module that creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """A function that creates an Object from a JSON file

    Args:
        filename: path to the JSON file to read from

    Returns:
        The Python object created from the JSON file
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
