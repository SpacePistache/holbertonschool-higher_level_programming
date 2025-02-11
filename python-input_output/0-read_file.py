#!/usr/bin/python3
"""This a module that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """
        A function that opens and reads the text in the .txt file

       Args:
           filename: this'll be the file that is accessed and read
    """


with open(filename, "r", encoding="utf-8") as file:
    print(file.read(), end="")
