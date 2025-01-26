#!/usr/bin/python3
"""
This module provides a function to format text by adding line breaks
after specific punctuation characters.

The text_indentation function processes input text, adding two newline
characters after periods, question marks, and colons while removing
unnecessary whitespace.
"""


def text_indentation(text):
    """
    Print text with line breaks after specific punctuation characters.

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If the input is not a string.

    Prints:
        Formatted text with two newlines after '.', '?', and ':',
        with no leading or trailing whitespace on each line.
    """
    # Validate input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Special punctuation characters that trigger line breaks
    special_chars = '.?:'

    # Process the text
    processed_text = ""
    for char in text:
        processed_text += char

        # Add two newlines after special characters
        if char in special_chars:
            processed_text += "\n\n"

    # Split lines and strip whitespace
    lines = processed_text.split('\n')

    # Print non-empty lines after stripping whitespace
    for line in lines:
        print(line.strip(), end='')
        if line.strip():
            print()
