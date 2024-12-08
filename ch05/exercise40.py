#!/usr/bin/python

#
# Chapter 05
#
# Exercise 40
#

import sys


class Morph:
    def __init__(self, token_and_info):
        info = token_and_info[1].split(",")
        self.surface = token_and_info[0]
        self.base    = info[-3]
        self.pos     = info[0]
        self.pos1    = info[1]


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
        print("------------------------")
        print("表層形:", morph.surface)
        print("基本形:", morph.base)
        print("品詞:", morph.pos)
        print("品詞細分類1:", morph.pos1)


if __name__ == "__main__":
    main()
