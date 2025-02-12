#!/usr/bin/python3
"""A module containing a class definig a student"""


class Student:

    def __init(self, first_name, last_name, age):
        """Initialization of attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary for student"""
        return self.__dict__
