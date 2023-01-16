#!/usr/bin/python3
"""
Module contains class Base
Contains private class __nb_objects, and class constructor __init__
Returns JSON string representation of list dictionaries
Saves JSON strings of instance dictionaries into file
Returns Python obj of JSON string representation
Returns instance with attributes already set
Returns list of instances
Saves to CSV and loads from CSV file
"""


import json
class Base:
    """
    defines class Base
    Class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
    Static Methods:
        to_json_string(list_dictionaries)   from_json_string(json_string)
    Class Methods:
        save_to_file(cls, list_objs)        save_to_file_csv(cls, list_objs)
        load_from_file(cls)                 load_from_file_csv(cls)
        create(cls, **dictionary)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id, increment class attribute if no id and set as id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string static method that returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file class method that writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            fileName = "{}.json".format(cls.__name__)
            objs = []
            for o in list_objs:
                objs.append(o.to_dictionary())

        with open(fileName, "w") as f:
                f.write(cls.to_json_string(objs))
                f.close()
