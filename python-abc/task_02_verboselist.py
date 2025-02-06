#!/usr/bin/python3
"""A module extending the Python list with notifications"""


class VerboseList(list):
    """Custom list that extends the Python list class"""

    def append(self, item):
        """Adds an element to the list and prints a notification"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list with multiple items & prints notification"""
        index = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{index}] items.")

    def remove(self, item):
        """Removes an item from the list and prints a notification"""
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Item [{item}] not found in list.")

    def pop(self, index=-1):
        """Another item removal function"""
        if self:
            item = self[index]
            print(f"Popped [{item}] from the list")
            return super().pop(index)
        else:
            print("Cannot pop from an empty list.")
            return None
