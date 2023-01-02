#!/usr/bin/python3

"""
Module 1-rectangle
Contains class Rectangle
Creates a rectangle object.
"""
class Rectangle:
    """
    Defines a rectangle with attributes
    """
    def __init__(self, width=0, height=0):
        """
        __init__ method for initializing Rectangle class.

        Args:
            width (int): Width of rectangle.
            height (int): Height of rectangle.
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Getter method for retrieving width or rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting new value of width attribute.

        Args:
            value (int): New value of width.

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving height of rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting new value of height attribute.

        Args:
            value (int): New value of height attribute.

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)


