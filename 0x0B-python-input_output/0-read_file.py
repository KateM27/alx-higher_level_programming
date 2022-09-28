#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """reads a text file and prints it out to stdout"""
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
