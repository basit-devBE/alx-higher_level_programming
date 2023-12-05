#!/usr/bin/python3
"""This is a module that writes a string to a
text file ad return the number of """


def write_file(filename="", text=""):
    """This function writes a string to the file and
    count the number of characters"""

    with open(filename, "w", encoding="uft-8") as f:
        return f.write(text)
