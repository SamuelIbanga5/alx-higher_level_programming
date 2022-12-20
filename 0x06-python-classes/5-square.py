#!/usr/bin/python3

"""My sixth python class (Square)."""

class Square:
    """Square class for creating squares or different sizes."""

    def __init__(self, size=0):
        """__init__ method for initiliazing square class.

        Args:
            size (int): Size of square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
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

    def area(self):
        """area method for calculating the area of a square.

        Returns:
            Area of square.

        """
        return self.__size * self.__size

    def my_print(self):
        """my_print method that prints the square with #."""
        
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("\n", end="")
        else:
            print("")

if __name__ == "__main__":
    Square = __import__('5-square').Square

    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
        
