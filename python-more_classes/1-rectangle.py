#!/usr/bin/python3
"""String representation............................."""


class Rectangle:
    """String representation.........................."""

    def __init__(self, width=0, height=0):
        """Initialize .
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """find the width of the rectangle..............."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """find the height of the rectangle.............."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
