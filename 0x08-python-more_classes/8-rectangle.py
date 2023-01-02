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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        __init__ method for initializing Rectangle class.
        Args:
            width (int): Width of rectangle.
            height (int): Height of rectangle.
        """
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

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
        print_rec = "\n".join([str(self.print_symbol) * self.__width for rows in range(self.__height)])
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
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        bigger_or_equal method for checking rectangle with largest area.

        Args:
            rect_1 (Rectangle, optional): First instance of Rectangle class
            rect_2 (Rectangle, optional): Second instance of Rectangle class

        Raises:
            TypeError: If rect_1 or rect_2 are not of Rectangle instances
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

if __name__ == "__main__":
    my_rectangle_1 = Rectangle(8, 4)
    my_rectangle_2 = Rectangle(2, 3)

    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")


    my_rectangle_2.width = 10
    my_rectangle_2.height = 5
    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")
