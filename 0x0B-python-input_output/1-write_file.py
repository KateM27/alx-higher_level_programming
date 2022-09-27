#!/usr/bin/python3
"""writes a string to a text file and returns the number of characters"""


def write_file(filename="", text=""):
    with open("filename", mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
