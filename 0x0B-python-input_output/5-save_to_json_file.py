#!/usr/bin/python3
"""
Module 5-save_to_json_file.py
Contains function that writes an object to a text file using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation
    Args:
        my_obj: Python object
        filename: Name of file
    """
    import json
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
