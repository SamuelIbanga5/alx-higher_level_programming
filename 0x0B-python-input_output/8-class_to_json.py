#!/usr/bin/python3
"""
Module 8-class_to_json
Contains function that returns the dictionary description
with simple data structure for JSON serializaiton of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    Args:
        obj: Python object
    Return:
        Dictionary description with simple data structure
    """
    return obj.__dict__
