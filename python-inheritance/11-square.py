#!/usr/bin/python3
"""
Defines a Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square with validated size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return "[Square] {}/{}".format(
                self._Rectangle__width, self._Rectangle__height)
