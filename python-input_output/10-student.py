#!/usr/bin/python3
"""Module that defines a Student class with filtered JSON serialization."""


class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes listed in attrs
        are included in the returned dictionary.
        """
        if isinstance(attrs, list):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__
