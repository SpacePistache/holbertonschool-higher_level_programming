#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:  # Check if the key exists
        del a_dictionary[key]  # Delete the key-value pair
    return a_dictionary  # Return the updated dictionary
