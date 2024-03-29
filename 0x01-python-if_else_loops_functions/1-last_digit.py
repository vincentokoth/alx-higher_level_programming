#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Ensure the last digit is negative for negative numbers
if number < 0:
    lastDigit = -(-number % 10)
else:
    lastDigit = number % 10

if lastDigit > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, lastDigit))
elif lastDigit == 0:
    print("Last digit of {} is {} and is 0"
          .format(number, lastDigit))
elif lastDigit < 6 and lastDigit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, lastDigit))
