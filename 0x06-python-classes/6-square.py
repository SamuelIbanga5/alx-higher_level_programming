#!/usr/bin/python3

"""My seventh python class (Square)"""

class Square:
    """Square class that creates squares with different sizes."""
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method for initiliazing square class.
        Args:
            size (int): Size of square.
            position (tuple): Coordinate or position of square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """size getter method for gettings value of size.

        Returns:
            Value of size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter method for setting value of size.
        Args:
            value (int): New value of size.
        Raises:
            TYpeError: if value is not an integer.
            ValueError: If value is less than 0.
        """
        self.__size = value
    
    @property
    def position(self):
        """position getter method for getting position or coordinate of a square.

        Returns:
            Tuple containing coordinate of the square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """position setter method for setting position of square.

        Args:
            value (tuple): TUple of two positive integer coordinates

        Raises:
            TypeError: If value is not a tuple of two positive integers.

        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """area method for calculating the area of a square.
        Returns:
            Area of square.
        """
        return self.__size * self.__size

    def my_print(self):
        """my_print method that prints the square with #."""

        if self.__size != 0:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print("")

if __name__ == '__main__':
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
