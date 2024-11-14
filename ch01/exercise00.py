#!/usr/bin/python

#
# Chapter 01
#
# Exercise 00
#

import sys


# Reverse string
def reverse_str(input_str):
    length = len(input_str)

    last_index = length - 1

    output_str = []
    for i in range(length):
        output_str.append(input_str[last_index - i])

    return "".join(output_str)


def main():
    args = sys.argv

    # Number of command line argments must be 1
    if len(args) != 2:
        print("Usage:\n", args[0], "string")
        exit(1)

    input_str = args[1]

    output_str = reverse_str(input_str)
    print(output_str)


if __name__ == "__main__":
    main()
