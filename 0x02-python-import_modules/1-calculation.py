#!/usr/bin/python3
# 1-calculation.py

if __name__ == "__main__":
    """Does some maths and prints the results"""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    print("10 + 5 = {}".format(add(a, b)))
    print("10 - 5 = {}".format(sub(a, b)))
    print("10 * 5 = {}".format(mul(a, b)))
    print("10 / 5 = {}".format(div(a, b)))
