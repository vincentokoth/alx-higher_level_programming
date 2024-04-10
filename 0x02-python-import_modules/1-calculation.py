#!/usr/bin/python3
# 1-calculation.py

if __name__ == "__main__":
    """Does some maths and prints the results"""
    import calculator_1 as calc

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, calc.add(a, b)))
    print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    print("{} / {} = {}".format(a, b, calc.div(a, b)))
