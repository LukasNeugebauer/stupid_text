#!/usr/bin/env python3
"""
Replace some letter with symbols and numbers
"""

import sys


mapping = {
    'a': '4',
    'A': '4',
    'c': '(',
    'C': '(',
    'e': '3',
    'E': '3',
    'g': '9',
    'G': '6',
    'H': '#',
    'i': '!',
    'I': '1',
    'j': '7',
    'J': '7',
    'l': '1',
    'o': '0',
    'O': '0',
    's': '5',
    'S': '5',
    't': '+',
    'z': '2',
    'Z': '2',
}
mapping = str.maketrans(mapping)


if __name__ == '__main__':
    string = sys.argv[1]
    print(string.translate(mapping))
