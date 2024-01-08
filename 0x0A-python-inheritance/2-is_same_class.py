#!/usr/bin/python3
# 2-is_same_class.py
"""defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check is an an object is exactly an instance of a given class

    Args:
    obj (any); The object to check.
    a_class (type); the class to match the type of obj to.
    returnsL
    If obj is exactly an instance of a_class - true
    otherwise - false
    """
    if type(obj) == a_class:
        return True
    return False
