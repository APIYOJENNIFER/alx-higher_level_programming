#!/usr/bin/python3
"""Create a Square class"""


class Square:
    """Square class initialization with a private instance attribute size
       Set size attribute with optional value of 0
       Raise TypeError if size is not an integer
       Raise ValueError if size is less than 0
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
