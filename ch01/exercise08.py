#!/usr/bin/python

#
# Chapter 01
#
# Exercise 08
#

import sys


def cipher(input_str):
    # Lowercase range
    lower_first = ord("a")
    lower_last = ord("z")

    input_str = list(input_str)
    for idx, char in enumerate(input_str):
        # ascii code of char
        code = ord(char)
        if lower_first <= code and code <= lower_last:
            input_str[idx] = chr(219 - code)

    return "".join(input_str)


def main():
    args = sys.argv

    # Number of command line argments must be 1
    if len(args) != 2:
        print("Usage:\n", args[0], "string")
        exit(1)

    input_str = args[1]

    encoded = cipher(input_str)
    print("Encode: ", encoded)

    decoded = cipher(encoded)
    print("Decode: ", decoded)


if __name__ == "__main__":
    main()
