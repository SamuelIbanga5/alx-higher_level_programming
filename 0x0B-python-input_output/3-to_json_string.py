#!/usr/bin/python3
import json
"""
Module 3-to_json_string
Contains function that returns the JSON representation of an object"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object."""
    return json.dumps(my_obj)
