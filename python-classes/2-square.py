#!/usr/bin/python3
""" This module will provide functionality for working with a square """


class Square:
    """ A class for a square """

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size <= 0:
            raise ValueError("size must be >= 0")

        self.__size = size


pass
