#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNum = abs(number) % 10
if number < 0:
    lastNum = -lastNum
if lastDigit == 0:
    print(f"Last digit of {number} is {lastNum} and is 0")
elif lastDigit > 5:
    print(f"Last digit of {number} is {lastNum} and is greater than 5")
else:
    print(f"Last digit of {number} is {lastNum} and is less than 6 and not 0")
