#!/usr/bin/python3
def print_last_digit (number):
    i = 10
    if (number < 0):
        i = -10
    print(number%i, end="")
    return number%i
