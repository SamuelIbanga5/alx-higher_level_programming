#!/usr/bin/python3
"""
Module 0-add_integer
Contains one method that returns an int sum
Accepts two values (a, b) whether int or float, and casts them to int
before adding.
"""

def add_integer(a, b=98):
    """Return the sum of two integers a and b.
    """
    sum = 0
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        sum = int(a) + int(b)
    return sum

if __name__ == "__main__":
    add_integer = __import__('0-add_integer').add_integer

    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
