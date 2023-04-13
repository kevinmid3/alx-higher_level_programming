#!/usr/bin/python3
""" This module contains a function that returns the JSON
representation of an object in python
"""
import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object
    Args:
        my_obj: object
    Raises:
        Exception: when the object can't be encoded
    """
    return json.dumps(my_obj)
