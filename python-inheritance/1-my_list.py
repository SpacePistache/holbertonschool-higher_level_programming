#!/usr/bin/python3
""" A class that inherits from a list and prints the list sorted"""


class MyList(list):
    """ Mylist inherits from list """

    def print_sorted(self):
        """ Prints list in ascending order, no OG list modification """

        print(sorted(self))
