#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    values = sorted(a_dictionary.values())
    for keys in a_dictionary:
        if a_dictionary[keys] == values[-1]:
            return keys
