#!/usr/bin/python3
"""
Module 0-read_file
Contains function that reads and prints contents from file
"""
def read_file(filename=""):
    """Read and print a text file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end='')
