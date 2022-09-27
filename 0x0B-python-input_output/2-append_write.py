#!/usr/bin/python3

def append_write(filename="", text=""):
    """appends a string at the end of a text file and returns the number of characters added"""
    with open("filename", mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
