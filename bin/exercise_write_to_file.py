#!/usr/bin/env python3.6

var_file = input("Filename: ")

with open(var_file,'a+') as f:
    loop = 1
    while loop != 0:
        var_text = input("Line to write: ")
        if var_text != '':
            f.write(var_text + "\n")
        else:
            loop = 0


