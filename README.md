# ASCIILines Challenge

## Purpose
This program represents a solution to a specific challenge, which is described below, as part of CS561 Open Source Software at Portland State University.

## The Challenge
_The problem description is adapted from Bart Massey's homework assignment found [here](https://moodle.cs.pdx.edu/mod/assign/view.php?id=114)._

Create a command-line program that will accept a single .tvg file argument and render the file as ASCII on standard output. Your program may fail on invalid input, but must panic or otherwise display an error in this case.

### The TVG Format
A "TVG" file contains "Text Vector Graphics".

The first line of the file contains the _canvas size_, which is the number of rows and columns of text to output (both must be greater than zero). The canvas starts out filled with `.` characters.

The rest of the file is rendering commands, one per line.

A rendering command is a line containing:

* A character to render with
* A row position to start at (0-based)
* A column position to start at (0-based)
* Either h for a horizontal line or v for a vertical line
* A length for the rendered line (must be greater than 0)
* The elements of the command should be separated by a single space.

The character positions that are part of the rendering command's rendered line should be filled with the rendering character. It is legal for the line to be outside the canvas; only points inside the canvas should be rendered.

A rendering output is produced by executing each of the rendering commands on the canvas. 

## Build and Run 
To run this command-line program, first open your terminal and complete the following steps:
1. First, git clone this asciilines repository: `git clone https://github.com/carissaallen/asciilines.git`
2. Then, `cd` (change directory) into asciilines.
3. Finally, enter the following command, replacing `your_file_path.tvg` with your own TVG file:
```
python3 asciilines.py your_file_path.tvg
```

## Usage
You may have a TVG file called _test2.tvg_ containing the following input:
```
7 7
A 1 2 h 1
B 5 2 v 1
C 2 6 h 1
D 2 3 v 1
```

By entering the following command (if asciilines.py is in your current directory):
```
python3 asciilines.py tests/test2.tvg
```

You will get an output that looks like this:
```
. . . . . . .
. . A . . . .
. . . D . . C
. . . . . . .
. . . . . . .
. . B . . . .
. . . . . . .
```

## Testing
_Information about bugs, defects, failing tests, etc._

## License
Copyright &copy; 2019 Carissa Allen

Licensed under the MIT License. See [the license](/LICENSE) for more information.
