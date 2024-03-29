#!/usr/bin/python3
"""
class LockedClass:
Defines a class with no class or object attributes
"""


class LockedClass:
    """
    Prevent the user from creating new instance attribute
    """

    __slots__ = ["first_name"]
