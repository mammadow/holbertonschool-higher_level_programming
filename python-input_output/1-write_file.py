#!/usr/bin/python3
"""Module that defines to write a string to a text file."""


def write_file(filename="", text=""):
    """Defines a function that writes to a file."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
