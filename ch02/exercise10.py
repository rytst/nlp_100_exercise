#!/usr/bin/python

#
# Chapter 02
#
# Exercise 10
#

import sys


def main():
    args = sys.argv

    # Number of command line argments must be 1
    assert len(args) == 2, "\nUsage: \n {} string".format(args[0])

    input_file = args[1]

    try:
        fp = open(input_file, 'r')
    except OSError:
        print("Could not open/read file:", input_file)
        sys.exit()

    with fp:
        # `Enumerate()` method adds a counter to an iterable
        # and returns it in the form of an enumerating object. 
        for count, _ in enumerate(fp):
            pass
        print(count + 1)



if __name__ == "__main__":
    main()
