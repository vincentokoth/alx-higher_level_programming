#!/usr/bin/python3
# 1-my_list.py
"""Defines an inherited list class myList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """print a list in sorted ascending order."""
        print(sorted(self))
