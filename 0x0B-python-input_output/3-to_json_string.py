#!/usr/bin/python3
"""
Module 3-to_json_string
Contains function that returns the JSON representation of an object"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object.
    Args:
        my_obj: Python object
    Return:
        json string representation
    """
    import json
    return json.dumps(my_obj)
