#!/usr/bin/python

#
# Chapter 02
#
# Exercise 15
#

import sys


def main():
    args = sys.argv

    # Number of command line argments must be 2
    assert len(args) == 3, "Usage: {} n filename".format(args[0])

    n = int(args[1])
    INPUT_FILE = args[2]

    try:
        fp = open(INPUT_FILE, "r")
    except OSError:
        print("Could not open/read file:", INPUT_FILE)
        sys.exit()

    with fp:

        n_lines = fp.readlines()[-n:]

        for line in n_lines:
            print(line, end="")


if __name__ == "__main__":
    main()
