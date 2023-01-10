#!/usr/bin/python3
"""
Module 6-load_from_json_file
Contains function that creates an OBject from JSON file
"""


def load_from_json_file(filename):
    """
    creates an Object from a JSON file
    Args:
        filename: Name of file
    """
    import json
    
    with open(filename, mode="r", encoding="utf-8") as f:
        return(json.load(f))
