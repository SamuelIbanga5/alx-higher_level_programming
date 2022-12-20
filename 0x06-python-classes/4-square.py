#!/usr/bin/python3
"""My fifth python class (Square)."""

class Square:
    """Square class for creating a square with different sizes."""

    def __init__(self, size):
        """__init__ method for initializing Square class.

        Args:
            size (int): Size of square.

       """
        self.__size = size

    def area(self):
        """area method for calculating area of square.

        Returns:
            Area of square.

        """

        return self.__size * self.__size

    @property
    def size(self):
        """size method returns the value of size attribute.

        Returns:
            Value of the size attribute.

        """

        return self.__size
    
    @size.setter
    def size(self, value):
        """size method with property setter for setting the value
        of size.

        Args:
            value (int): size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


if __name__ == "__main__":
    Square = __import__('4-square').Square

    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)

