#!/usr/bin/python3
"""This a module that reads a text file and prints it to stdout"""


def write_file(filename="", text=""):
    """A function that opens and reads the text in the .txt file"""


with open("my_file_0.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)
file.close()
