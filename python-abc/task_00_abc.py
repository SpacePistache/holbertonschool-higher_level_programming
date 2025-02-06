#!/usr/bin/python3
"""This Module defines an animal class and some instances of animals."""


from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        """Method to be implemented in subclasses."""
        pass


class Dog(Animal):
    """A child class from Animal, WOOF!"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Second Child class from Animal, MEOW!"""
    def sound(self):
        return "Meow"
