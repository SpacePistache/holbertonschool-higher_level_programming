#!/usr/bin/python3
"""A module that appends to a .txt file"""


def append_write(filename="", text=""):
    """A function that appends to a .txt file

        Args:
            filename: will be that document that is modified.
            text: The text that will be added.
        Returns:
            Characters written
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
