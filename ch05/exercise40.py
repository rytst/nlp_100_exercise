#!/usr/bin/python

#
# Chapter 05
#
# Exercise 40
#

import sys


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


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
        for line in fp.readlines():
            line = line.strip()  # Remove new line
            if line[0] == "*":
                continue

            token_and_info = line.split()  # Split by space

            token = token_and_info[0]
            if token == "EOS":
                morph_list.append(token)
                continue

            # Get information from text data
            surface = token
            base = token_and_info[1][-3]
            pos = token_and_info[1][0]
            pos1 = token_and_info[1][1]

            # Create instance
            morph = Morph(surface, base, pos, pos1)
            morph_list.append(morph)

    # Print expected data
    for morph in morph_list:
        if morph == "EOS":
            continue
        print(morph.surface, ":    ", morph.pos)


if __name__ == "__main__":
    main()
