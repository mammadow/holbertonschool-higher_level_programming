#!/usr/bin/python3
"""
Defines a function that adds a new attribute to an object if possible.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it is allowed.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
