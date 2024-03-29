#!/usr/bin/pyhon
# 2-append_write.py
"""Defines a file appending function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters to append.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
