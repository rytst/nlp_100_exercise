#!/usr/bin/python

#
# Chapter 02
#
# Exercise 16
#

import sys


def main():
    args = sys.argv

    # Number of command line argments must be 2
    assert len(args) == 3, "Usage: {} n filename(to split)".format(args[0])

    n = int(args[1])
    INPUT_FILE = args[2]

    # Try to read file
    try:
        fp = open(INPUT_FILE, "r")
    except OSError:
        print("Could not open/read file:", INPUT_FILE)
        sys.exit()

    with fp:
        for idx, line in enumerate(fp.readlines()):
            # ex: splitted0.txt, splitted1.txt, ...
            OUTPUT_FILE = "splitted{}.txt".format(idx % n)

            # Try to write data to file
            try:
                # Initialization
                if idx < n:
                    open(OUTPUT_FILE, "w").close()

                fp = open(OUTPUT_FILE, "a")
                fp.write(line)
                fp.close()
            except OSError:
                print("Could not open/write file:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
