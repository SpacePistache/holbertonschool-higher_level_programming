#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase without using str.upper()."""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:  # Check if char is lowercase
            char = chr(ord(char) - 32)  # Convert to uppercase
        print("{:s}".format(char), end="")
    print("")  # Print a newline at the end
