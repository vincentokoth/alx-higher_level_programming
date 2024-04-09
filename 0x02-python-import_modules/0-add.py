#!/usr/bin/python3
if __name__ == "__main__":
    a, b = 1, 2

    from add_0 import add

    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
