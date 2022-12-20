#!/usr/bin/python3
"""My second python class (Square)"""
class Square:
    """Square class for creating squares with different sizes"""

    def __init__(self, size):
        """__init__ method for initializing a class.

        Args:
            size (int): Specifies the size of square.

        """
        self.__size = size


if __name__ == '__main__':
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
