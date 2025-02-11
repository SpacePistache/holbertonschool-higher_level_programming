#!/usr/bin/python3
"""A module that writes a string to txt file"""


def write_file(filename="", text=""):
    """A function that writes a string to a .txt file

        Args:
            filename: will be that document that is modified.
            text: The text that will be added.
        Returns:
            None
    """

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
