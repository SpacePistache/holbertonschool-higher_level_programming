#!/usr/bin/python3
def text_indentation(text):
    """
    Function prints text with two new lines after: `.`, `?`, and `:`.
    Text processed without leading/trailing spaces after each printed line.

    Args:
    text (str): The input string to be processed.

    Raises:
    TypeError: If `text` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # We will loop through the text and print accordingly
    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:  # Check if the character is one of the target ones
            print(text[i].strip())  # Print the character itself, then add two newlines
            print()  # Add the first newline
            print()  # Add the second newline
            i += 1  # Move to the next character
        else:
            print(text[i], end="")  # Print the character without new line
            i += 1  # Move to the next character
