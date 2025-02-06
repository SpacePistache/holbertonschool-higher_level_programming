#!/usr/bin/python3
"""A module creating an iterator to count iterations"""


class CountedIterator:
    """An iterator that counts iterations."""

    def __init__(self, iteration):
        """Initialization of iteration counter"""
        self.iterator = iter(iteration)
        self.count = 0  # Changed from self.index to self.count

    def __iter__(self):
        """Returns self as iterable"""
        return self

    def __next__(self):
        """Moves on to next item and counts"""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """Return the total number of items iterated over."""
        return self.count
