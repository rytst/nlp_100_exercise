#!/usr/bin/python

#
# Chapter 05
#
# Exercise 40
#

import sys


class Morph:
    def __init__(self, token_and_info):
        self.surface = token_and_info[0]
        self.base = token_and_info[1][-3]
        self.pos = token_and_info[1][0]
        self.pos1 = token_and_info[1][1]


def main():
    args = sys.argv

    # Number of command line argments must be 1
    assert len(args) == 2, "Usage: {} file".format(args[0])
    file_name = args[1]

    try:
        fp = open(file_name, "r")
    except OSError:
        print("Could not read {} ...".format(file_name))
        sys.exit()

    morph_list = list()
    with fp:
        for line in fp.read().splitlines():
            if line[0] == "*":
                continue

            token_and_info = line.split()  # Split by space

            token = token_and_info[0]
            if token == "EOS":
                morph_list.append(token)
                continue

            # Create instance
            morph = Morph(token_and_info)
            morph_list.append(morph)

    # Print expected data
    for morph in morph_list:
        if morph == "EOS":
            continue
        print(morph.surface, ":    ", morph.pos)


if __name__ == "__main__":
    main()
