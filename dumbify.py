#!/usr/bin/python3
"""
Turn any string into dumb talk
"""


import sys


def dumbify(string):
    counter = 0
    out = ""
    funs = [str.lower, str.upper]
    for letter in string:
        if not letter.isalpha():
            out += letter
        else:
            out += funs[counter % 2](letter)
            counter += 1
    return out


if __name__ == '__main__':
    print(dumbify(sys.argv[1]))
