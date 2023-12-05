#!/usr/bin/python3
"""This module defines a function that reads a text
    """

def read_file(filename=""):
    """prints the content if the file

    Args:
        filename (str, optional)._the name of the file_. Defaults to "".
    """
    
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")