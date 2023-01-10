#!/usr/bin/python3
"""
Module 1-write_file
Contains function that writes to a text file and returns num chars written
"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return(f.write(text))
