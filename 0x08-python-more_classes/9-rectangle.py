#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)"""


class Rectangle:
    """signifies a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """rectangle class is being initialized
        Args:
            width: rectangle's width
            height: rectangle's height
        Note:
            width must be an integer, otherwise raise a TypeError
            if height is less than 0, raise a ValueError
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width attribute is retrieved"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height attribute is retrieved"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

