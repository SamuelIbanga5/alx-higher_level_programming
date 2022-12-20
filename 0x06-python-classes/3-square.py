#!/usr/bin/python3
"""My fourth class (Square)."""

class Square:
    """Square class for creating squares with different sizes."""

    def __init__(self, size=0):
        """__init__ method for initializing Square class.

        Args:
            size (int): Size of square.

        Returns:
            The current square area.

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """area method for calculating the area of square."""

        return  self.__size * self.__size

if __name__ == "__main__":
    Square = __import__('3-square').Square

    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
