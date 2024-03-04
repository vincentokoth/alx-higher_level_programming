#!/usr/bin/python3
def uppercase(str):
    """In ASCII, the difference between lowercase and uppercase letters
       is 32. We can therefore convert characters to uppercase using
       their ASCII codes by subtracting ASCII value difference between
       the uppercase and lowercase letters.
    """
    uppercase_str = ""

    if not str:  # if the string is empty
        raise ValueError("input string cannot be empty")
    for char in str:
        if 'a' <= char <= 'z':  # check if the char is lowercase
            uppercase_str += chr(ord(char) - 32)
        else:
            uppercase_str += char
    return uppercase_str
