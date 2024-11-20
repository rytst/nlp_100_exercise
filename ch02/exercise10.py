#!/usr/bin/python

#
# Chapter 02
#
# Exercise 10
#

import sys

INPUT_FILE = "popular-names.txt"


def main():
    try:
        fp = open(INPUT_FILE, "r")
    except OSError:
        print("Could not open/read file:", INPUT_FILE)
        sys.exit()

    with fp:
        # `Enumerate()` method adds a counter to an iterable
        # and returns it in the form of an enumerating object.
        for count, _ in enumerate(fp):
            pass
        print(count + 1)


if __name__ == "__main__":
    main()
