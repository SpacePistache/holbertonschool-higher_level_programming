#!/usr/bin/python3
"""This a module that reads a text file and prints it to stdout"""


def write_file(filename="", text=""):

    with open("my_file_0.txt", "r", encoding="utf-8"):
        content = content.read()
        print(content)
    content.close