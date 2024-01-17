#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number[-1]
print("Last digit of", number, "is", last_digit)
print(last_digit > 5 ? "and is greater than 5")
print(last_digit == 0 ? "and is 0")
print(last_digit < 6 and not 0 ? "and is less than 6 and not 0")
