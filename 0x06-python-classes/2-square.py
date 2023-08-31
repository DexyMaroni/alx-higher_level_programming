#!/usr/bin/python3

"""Defines A Class Square."""



class Square:
    """Represents A Square"""

    def __init__(self, size=0):
        """Initializes A New Square>


        Args:
            size (int); The size of a new square.

        """


        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
