#!/usr/bin/python3
"""
Module 7-add_item
Script that adds all arguments to a python list, and then save them to a file
"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

import sys
new_list = sys.argv[1:]
fileName = "add_item.json"


try:
    existingContent = load_from_json_file(fileName)
except FileNotFoundError:
    existingContent = []

save_to_json_file(existingContent + new_list, fileName)
