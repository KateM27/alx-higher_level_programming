#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using json representation"""
    with open("filename", mode="w", encoding="utf-8") as myFile:
        return json.dump(my_obj, myFile)
