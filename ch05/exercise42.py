#!/usr/bin/python

#
# Chapter 05
#
# Exercise 42
#

import sys
import re
from collections import deque
from copy import deepcopy


class Morph:
    def __init__(self, token_and_info):
        self.surface = token_and_info[0]
        self.base    = token_and_info[1][-3]
        self.pos     = token_and_info[1][0]
        self.pos1    = token_and_info[1][1]

class Chunk:
    morphs = list()

    # Set dst and srcs
    def setup(self, dependency_info):
        info_list = dependency_info.split()
        dst = re.findall(r"-?\d+", info_list[2])

        self.dst  = int(dst[0])
        self.srcs = info_list[1]

    # Add morph to morphs
    def add_morph(self, morph):
        self.morphs.append(morph)

    # Reset member variable
    def reset(self):
        self.morphs = list()
        self.dst    = None
        self.srcs   = None

    # Print member variable
    def show(self):
        print("dst: {}, srcs: {}".format(self.dst, self.srcs))
        for morph in self.morphs:
            print(morph.surface)

# Generate chunk_list
def make_chunk_list(fp):

    chunk_list = list()
    with fp:
        q = deque(fp.read().splitlines())

        chunk = Chunk()
        while len(q) > 0:
            elem = q.popleft()
            if elem == "EOS":
                chunk_list.append("EOS")
                continue

            # Set dependency information
            if elem[0] == "*":
                chunk.setup(elem)
                continue
            token_and_info = elem.split()
            morph = Morph(token_and_info)
            chunk.add_morph(morph)

            # If the token is end of chunk,
            # add the chunk to chunk_list
            next = q[0]
            if next == "EOS" or next[0] == "*":
                chunk_list.append(deepcopy(chunk))
                chunk.reset()
    return chunk_list


# Print chunk_list
def print_chunk_list(chunk_list):
    for chunk in chunk_list:
        if chunk == "EOS":
            print("EOS")
            continue
        chunk.show()

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

    chunk_list = make_chunk_list(fp)
    print_chunk_list(chunk_list)




if __name__ == "__main__":
    main()
