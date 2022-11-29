#!/usr/bin/python3
for numbers in range(0, 100):
    if numbers != 99:
        print("{:02d}".format(numbers), end=", ")
    elif numbers == 99:
        print("{:d}".format(numbers), end="\n")
