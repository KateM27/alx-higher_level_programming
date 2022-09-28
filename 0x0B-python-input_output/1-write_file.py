#!/usr/bin/python3
"""write_file function"""


def write_file(filename="", text=""):
    """writes a str to a txt file, returns the number of characters"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
