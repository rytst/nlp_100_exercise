#!../venv/bin/python

#
# Chapter 02
#
# Exercise 14
#

import sys

def main():

    args = sys.argv

    # Number of command line argments must be 2
    assert len(args) == 3, "Usage: {} n filename".format(args[0])

    n           = int(args[1])
    INPUT_FILE  = args[2]

    try:
        fp = open(INPUT_FILE, "r")
    except OSError:
        print("Could not open/read file:", INPUT_FILE)
        sys.exit()

    with fp:
        # The readlines() read all the lines in a single go and
        # then return them as each line is a string element in a list
        for idx, line in enumerate(fp.readlines()):
            print(line, end="")

            if idx+1 == n:
                break

if __name__ == "__main__":
    main()
