#!/usr/bin/python3
def islower(c):
    if not c:  # If the char is empty
        raise ValueError("Input string cannot be empty")
    for char in c:
        if ord(c) in range(97, 123):
            return 1
        else:
            return 0
