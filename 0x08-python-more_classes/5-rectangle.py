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

    def area(self):
        """
        Area method to calculate area of a rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Perimeter method to calculate perimeter of a rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * ( self.__height + self.__width )

    def __str__(self):
        """
        Printing the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        print_rec = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return print_rec

    def __repr__(self):
        """
        Printing string representation to recreate new instance
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method to delete an instance of Rectangle
        """
        print("Bye rectangle...")

if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
    
    del my_rectangle
    
    try:
        print(my_rectangle)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
