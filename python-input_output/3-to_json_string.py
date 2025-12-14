#!/usr/bin/python3
"""
Module that defines a function to return the JSON representation of an object.
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation (string) of a Python object."""
    return json.dumps(my_obj)
