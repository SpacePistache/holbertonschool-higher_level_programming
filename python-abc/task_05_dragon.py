#!/usr/bin/python3
"""A module demonstrating mixins with a Dragon class."""


class SwimMixin:
    """A mixin for swimming ability."""

    def swim(self):
        """Prints that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """A mixin for flying ability."""

    def fly(self):
        """Prints that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A mythical dragon with swimming and flying abilities."""

    def roar(self):
        """Prints that the dragon roars."""
        print("The dragon roars!")


if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()  # Outputs: The creature swims!
    dragon.fly()   # Outputs: The creature flies!
    dragon.roar()  # Outputs: The dragon roars!
