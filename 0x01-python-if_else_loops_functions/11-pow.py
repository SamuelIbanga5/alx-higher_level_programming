#!/usr/bin/python3
def pow(a, b):
    pow = 1
    for i in range(abs(b)):
        pow *= a
    if b < 0:
        pow = 1 / pow
    return pow
