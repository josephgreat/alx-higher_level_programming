#!/usr/bin/python3
"""Creates an initialized class"""


class Square:
    """Square class with initialization
    Attributes:
        size: private attribute
    """
    def __init__(self, size):
        """Iinitializing Square instance
        Args:
            size: number of size of square
        """
        self.__size = size
