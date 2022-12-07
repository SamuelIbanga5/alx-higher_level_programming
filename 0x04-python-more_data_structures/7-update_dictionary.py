#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
    elif key not in a_dictionary:
        a_dictionary[key] = value
    new_dict = {}
    for key in a_dictionary:
        new_dict[key] = a_dictionary[key]
    return new_dict
