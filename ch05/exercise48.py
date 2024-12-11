#!/usr/bin/python

#
# Chapter 05
#
# Exercise 48
#

import sys
import re
from collections import deque
from copy import deepcopy


class Morph:
    def __init__(self, token_and_info):
        info = token_and_info[1].split(",")
        self.surface = token_and_info[0]
        self.base    = info[-3]
        self.pos     = info[0]
        self.pos1    = info[1]


class Chunk:
    morphs = list()

    # Set dst and srcs
    def setup(self, dependency_info):
        info_list = dependency_info.split()
        dst = re.findall(r"-?\d+", info_list[2])

        self.dst  = int(dst[0])
        self.srcs = int(info_list[1])

    # Add morph to morphs
    def add_morph(self, morph):
        self.morphs.append(morph)

    # Reset member variable
    def reset(self):
        self.morphs = list()
        self.dst = None
        self.srcs = None

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


def get_chunk_txt(chunk):
    txt = ""
    for morph in chunk.morphs:
        if morph.pos == "記号":
            continue
        txt += morph.surface
    return txt

# idx is necessary to specify chunk
def find_chunk_by_dst(chunk_list, dst, idx):

    i = 0
    i_end_flag = False

    j = 0
    j_end_flag = False
    while True:
        chunk_forward = chunk_list[idx+i]
        chunk_backward = chunk_list[idx+j]

        if chunk_forward == "EOS":
            i_end_flag = True
        else:
            i += 1

        if chunk_backward == "EOS":
            j_end_flag = True
        else:
            j -= 1

        if not i_end_flag:
            if chunk_forward.srcs == dst:
                return chunk_forward

        if not j_end_flag:
            if chunk_backward.srcs == dst:
                return chunk_backward

        if i_end_flag and j_end_flag:
            print("Could not find dst ...")
            sys.exit()

def have_pos(chunk, pos):
    for morph in chunk.morphs:
        if morph.pos == pos:
            return True
    return False


def path_to_root(chunk, chunk_list, idx, result=""):

    srcs = chunk.srcs
    dst  = chunk.dst
    srcs_txt  = get_chunk_txt(chunk)

    if dst == -1:
        return result + srcs_txt

    dst_chunk = find_chunk_by_dst(chunk_list, dst, idx)

    result = result + srcs_txt + "->"
    return result + path_to_root(dst_chunk, chunk_list, idx)


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

    for idx, chunk in enumerate(chunk_list):

        # If chunk is "EOS" then, skip "EOS"
        if chunk == "EOS":
            continue

        srcs = chunk.srcs
        dst  = chunk.dst
        # If there is no destination, then skip the chunk
        if dst == -1:
            continue

        if not have_pos(chunk, "名詞"):
            continue

        path = path_to_root(chunk, chunk_list, idx)

        print(path, "\n")




if __name__ == "__main__":
    main()
