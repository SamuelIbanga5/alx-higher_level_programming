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
import csv
import turtle
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

    @staticmethod
    def from_json_string(json_string):
        """from_json_string static method that returns the list of the JSON string representation of json_string"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create class method returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load_from_file class method returns a list of instances"""
        fileName = "{}.json".format(cls.__name__)
        list_instance = []
        try:
            with open(fileName, "r") as file:
                instances = cls.from_json_string(file.read())
            for i, dic in enumerate(instances):
                list_instance.append(cls.create(**instances[i]))
        except:
            pass
        return list_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv class method that serializes in CSV"""
        fileName = "{}.csv".format(cls.__name__)
        with open(fileName, "w", newline="") as file:
            writer = csv.writer(file)
            for objs in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([objs.id, objs.width, objs.height, objs.x, objs.y])
                if cls.__name__ == "Square":
                    writer.writerow([objs.id, objs.width, objs.x, objs.y])

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file_csv class method that deserializes in CSV"""
        objs = []
        fileName = "{}.csv".format(cls.__name__)
        with open(fileName, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }
                if cls.__name__ == "Square":
                    dic = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }
                o = cls.create(**dic)
                objs.append(o)
        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
