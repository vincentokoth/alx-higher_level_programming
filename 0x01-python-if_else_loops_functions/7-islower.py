#!/usr/bin/python3
def islower(c):
    for char in c:
        if ord(c) in range(97, 123):
            return 1
        else:
            return 0
