#!/usr/bin/python3
"""load_from_json_file function"""
import json


def load_from_json_file(filename):
    """creates an object from a json file"""
    with open(filename, mode="r", encoding="utf-8") as myFile:
        return json.load(myFile)
