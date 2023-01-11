#!/usr/bin/python3
# File: 8-class_to_json.py
# Author: Vincent Okoth
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represenation of a simple data structure."""
    return obj.__dict__
