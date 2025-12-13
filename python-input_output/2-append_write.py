#!/usr/bin/python3
"""Module to define a function that appends string to a text file."""


def append_write(filename="", text=""):
    """Defines a function that appends to text file."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
