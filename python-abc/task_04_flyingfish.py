#!/usr/bin/python3
"""A module applying the concept of multiple inheritance"""


class Fish:
    """It's a fish..."""

    def swim(self):
        """Typical behaviour for a fish, to swim"""
        print("The fish is swimming")

    def habitat(self):
        """This is the fish's hometown"""
        print("The fish lives in water")


class Bird:
    """A type of flying fish, but it's not a fish but a bird"""

    def fly(self):
        """Flying, like swimming but it's in the air with more flapping"""
        print("The bird is flying")

    def habitat(self):
        """Where the bird hangs out"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A Frankenstein combination of the two animals"""

    def fly(self):
        """Is it a bird, is it a plane!?"""
        print("The flying fish is soaring!")

    def swim(self):
        """It's not a Russian nuclear submarine"""
        print("The flying fish is swimming")

    def habitat(self):
        """The flying fish doesn't compromise, it lives wherever it wants!"""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()

    print([cls.__name__ for cls in FlyingFish.mro()])
