#!/usr/bin/python

#
# Chapter 01
#
# Exercise 07
#

import sys


# Generate simple text
def gen_text(x, y, z):
    return x + "時の" + y + "は" + z



def main():
    args = sys.argv

    # Number of command line argments must be 1
    if len(args) != 4:
        print("Usage:\n", args[0], 'x', 'y', 'z')
        exit(1)

    x = args[1]
    y = args[2]
    z = args[3]

    output_str = gen_text(x, y, z)
    print(output_str)




if __name__ == "__main__":
    main()
