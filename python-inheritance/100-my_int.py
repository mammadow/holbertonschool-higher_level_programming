#!/usr/bin/python3
"""
Defines a MyInt class that inverts == and != operators.
"""


class MyInt(int):
    """
    Rebel integer class that inverts equality operators.
    """

    def __eq__(self, other):
        """
        Inverts == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts != operator.
        """
        return super().__eq__(otherg
