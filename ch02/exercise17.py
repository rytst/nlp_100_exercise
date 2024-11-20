#!/usr/bin/python

#
# Chapter 02
#
# Exercise 17
#

import sys

INPUT_FILE = "col1.txt"


def main():
    try:
        fp = open(INPUT_FILE, "r")
    except OSError:
        print("Could not open/read file:", INPUT_FILE)
        sys.exit()

    with fp:
        # The readlines() read all the lines in a single go and
        # then return them as each line is a string element in a list
        for line in sorted(set(fp.readlines())):
            print(line, end='')

if __name__ == "__main__":
    main()
