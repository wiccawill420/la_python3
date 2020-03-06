#!/usr/bin/env python3.6

import sys
import argparse

parser = argparse.ArgumentParser(description='Reads given line from file')
parser.add_argument('filename', help='the file to read')
parser.add_argument('linenum', type=int, help='the line from the file')

args = parser.parse_args()

try:
    with open(args.filename, 'r') as f:
        var_line = args.linenum - 1
        if var_line < 0:
            var_line = 1
        lines=f.readlines()
        try:
            print(lines[var_line], end = '')
        except IndexError as err:
            print(f"Error: File does not contain that many lines")
            sys.exit(1)
except FileNotFoundError as err:
    print(f"Error: File does not exist, idiot")
    sys.exit(1)

