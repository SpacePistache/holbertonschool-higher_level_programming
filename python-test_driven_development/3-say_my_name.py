#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    This function prints "My name is <first_name> <last_name>", where 
    first_name and last_name must be strings. If any of the inputs 
    are not strings, a TypeError is raised.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}".strip())
