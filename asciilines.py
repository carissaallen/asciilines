#!/usr/bin/env python 3
"""
asciilines.py
A command-line program that accepts a single TVG file argument, and renders the
file as ASCII on standard output.

The TVG file contains the following:
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
    """Returns an error if the given canvas size is invalid."""
    if len(canvas_size) != 2:
        print(
            "Error parsing file. Canvas size must include a row size and column size."
        )
        sys.exit()
    elif rows < 1 or cols < 1:
        print("Error parsing file. Rows and columns must be a minimum size of 1.")
        sys.exit()


def get_original_canvas(file_contents):
    """Fills the canvas with dots based on the canvas size given in the file contents."""
    canvas_size = file_contents[0].split(" ")
    rows = int(canvas_size[0])
    cols = int(canvas_size[1])
    validate_canvas(canvas_size, rows, cols)
    dots = " . "
    canvas = [[dots] * cols for i in range(rows)]
    return canvas


def validate_command(command):
    """Returns an error if there are not exactly 5 commands."""
    if len(command) != 5:
        print("Error parsing file. Command may not be properly formatted.")
        sys.exit()


def translate_commands(canvas, file_contents):
    """Translates the canvas given in the TVG file to ASCII, as directed by the rendering commands."""
    canvas_size = file_contents[0].split(" ")
    total_rows = int(canvas_size[0])
    total_cols = int(canvas_size[1])
    for line in range(1, len(file_contents)):
        command = file_contents[line].split(" ")
        validate_command(command)

        char_to_render = command[0]
        row_pos = int(command[1])
        col_pos = int(command[2])
        direction = command[3]
        length = int(command[4])

        if direction == "h":
            if row_pos > -1 and row_pos < total_rows:
                for i in range(length):
                    if (col_pos + i) > -1 and (col_pos + i) < total_cols:
                        canvas[row_pos][col_pos + i] = " " + char_to_render + " "
        elif direction == "v":
            if col_pos > -1 and col_pos < total_cols:
                for i in range(length):
                    if (row_pos + i) > -1 and (row_pos + i) < total_rows:
                        canvas[row_pos + i][col_pos] = " " + char_to_render + " "
        else:
            print("Error parsing file.")
            sys.exit()

    return canvas


def display_canvas(canvas):
    """Prints the canvas to the console."""
    for row in canvas:
        for cell in row:
            print(cell, end="")
        print()


def main():
    file_contents = get_tvg_file()
    canvas = get_original_canvas(file_contents)
    ascii = translate_commands(canvas, file_contents)
    display_canvas(ascii)


if __name__ == "__main__":
    main()
