#!/usr/bin/python3
"""
Module provides a function to process and print text with specific formatting.

The text_indentation function handles text printing with precise spacing
and punctuation-based line breaks, ensuring clean and consistent output.
"""


def text_indentation(text):
    """
    Print text with specific formatting rules.

    Args:
        text (str): The input text to be processed and printed.

    Raises:
        TypeError: If the input is not a string.

    Prints:
        Formatted text with controlled spacing and line breaks.
    """
    # Validate input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Special punctuation characters that trigger line breaks
    special_chars = '.?:'

    # Flag to track if we need to skip leading spaces
    skip_spaces = True

    # Process and print the text
    for char in text:
        if char == ' ' and skip_spaces:
            continue

        # Reset skip_spaces flag when non-space character is encountered
        skip_spaces = False

        # Print the character
        print(char, end='')

        # Add line breaks after special characters
        if char in special_chars:
            print('\n')
            skip_spaces = True
