#!/usr/bin/python3
"""returns the dictionary representation with
simple data structure for json serialization of an object"""


def class_to_json(obj):
    return obj.__dict__
