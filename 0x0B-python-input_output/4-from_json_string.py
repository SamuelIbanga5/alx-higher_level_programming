#!/usr/bin/python3
"""
Module 4-from_json_string
Contains function that returns an object represented by a JSON string"""


def from_json_string(my_str):
    """
    Returns an object(python data structure) represented by a JSON string
    Args:
        my_str: Python string object
    Return:
        Object represented by python string.
    """
    import json
    return json.loads(my_str)
