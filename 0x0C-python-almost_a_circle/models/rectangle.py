#!/usr/bin/python3
"""
Module contains class Rectangle
Inherits from Base;
Inits superclass' id
Contains private width, height, x, y
Contains public method area
Displays rectangle using "#"'s
Prints [Rectangle] (<id>) <x>/<y> - <width>/<height>
Updates attributes: arg1=id, arg2=width, arg3=height, arg4=x, arg5=y
Returns dictionary representation of attributes
"""

from base import Base

class Rectangle(Base):
    """
    defines class Rectangle; inherits from class Base
    Inherited Attributes:
        id
    Class Attributes:
        __width          __height
        __x              __y
    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
        update(self, *args, **kwargs)
        width(self)      width(self, value)
        height(self)     height(self, value)
        x(self)          x(self, value)
        y(self)          y(self, value)
        area(self)       display(self)
        __str__          to_dictionary(self)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @property
    def x(self):
        """Getter method for x value"""
        return self.__x

    @property
    def y(self):
        """Getter method for y value"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value <= 0:
                raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value <= 0:
                raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """Setter method for x value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        else:
            if value < 0:
                raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Setter method for y value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Area method for calculating area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """display function prints in stdout the rectangle instance with the character #"""
        print("\n" * self.__y, end="")
        for x in range(self.__height):
            print(" " * self.__x, end="")
            for y in range(self.__width):
                print("#", end="")
            print("\n", end="")

    def __str__(self):
        """print string representation of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
