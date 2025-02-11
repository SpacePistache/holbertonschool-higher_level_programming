#!/usr/bin/python3
"""A module that that creates an Object from a JSON file."""


import json


def load_from_json_file(filename):
    """A function that that creates an Object from a “JSON file”.

       Args:
            filename: the destination file.

       Return:
              .

    """
    with open(filename, "r", encoding="utf-80") as file:
            return json.load(file)
