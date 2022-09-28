#!/usr/bin/python3
"""append_write function"""


def append_write(filename="", text=""):
    """returns the number of characters added after a str is appended"""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
