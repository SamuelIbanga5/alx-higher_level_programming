#!/usr/bin/python3
"""
Module 2-append_write
This contains function that appends a string to an existing text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file and returns the number of characters added."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
