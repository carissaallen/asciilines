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
3. A column position to start at (0-based)
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
    """Accepts a TVG file as a command-line argument."""
    validate_args(len(sys.argv))
    filename = sys.argv[1]
    file = open(filename, "r")
    file_contents = file.readlines()
    file.close()
    return file_contents


def validate_canvas(canvas_size, rows, cols):
    if len(canvas_size) != 2:
        print(
            "Error parsing file. Canvas size must include a row size and column size."
        )
        sys.exit()
    elif rows < 1 or cols < 1:
        print("Error parsing file. Rows and columns must be a minimum size of 1.")
        sys.exit()


def get_original_canvas():
    file_contents = get_tvg_file()
    canvas_size = file_contents[0].split(" ")
    rows = int(canvas_size[0])
    cols = int(canvas_size[1])
    validate_canvas(canvas_size, rows, cols)
    dots = " . "
    canvas = [[dots] * cols for i in range(rows)]
    return canvas


def display_canvas(canvas):
    for row in canvas:
        for cell in row:
            print(cell, end="")
        print()


def main():
    canvas = get_original_canvas()
    display_canvas(canvas)
    print(canvas)


if __name__ == "__main__":
    main()
