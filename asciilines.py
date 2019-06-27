#!/usr/bin/env python 3
"""
asciilines.py
A command-line program that accepts a single .tvg file argument, and renders the
file as ASCII on standard output.

The .tvg file contains the following:
The first line contains the 'canvas size', or number of rows and columns of text 
to output (starts out filled with . characters)

Each subsequent line contains the following commands:
1. A character to render
2. A row position to start at (0-based)
3 A column position to start at (0-based)
4. Either 'h' for a horizontal line or a 'v' for a vertical line
5. A length for the rendered line (must be greater than 0)
"""

import sys


def validate_args(num_args):
    """Returns an error and exits the program if given an invalid number of arguments."""
    if num_args == 1:
        print("Please include the path to a single file as a command-line argument.")
        sys.exit()
    elif num_args > 2:
        print("Too many arguments entered. Please enter the path to a single file.")
        sys.exit()


def get_tvg_file():
    """Accept a TVG file as a command-line argument."""
    validate_args(len(sys.argv))
    filename = sys.argv[1]
    file = open(filename, "r")
    file_contents = file.readlines()
    file.close()
    return file_contents


def main():
    tvg_file = get_tvg_file()
    print(tvg_file)


if __name__ == "__main__":
    main()
