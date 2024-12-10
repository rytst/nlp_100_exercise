#!/usr/bin/python

#
# Chapter 05
#
# Exercise 47
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

def get_srcs_chunk_list(chunk_list, dst, idx):
    srcs_chunk_list = list()

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
            if chunk_forward.dst == dst:
                srcs_chunk_list.append(chunk_forward)

        if not j_end_flag:
            if chunk_backward.dst == dst:
                srcs_chunk_list.append(chunk_backward)

        if i_end_flag and j_end_flag:
            return srcs_chunk_list

# Write line to file
def write_line(line, file):
    try:
        fp = open(file, "a")
    except OSError:
        print("Could not open file ...")
        sys.exit()

    with fp:
        fp.write(line)


def get_postpositional(chunk):
    for morph in reversed(chunk.morphs):
        if morph.pos == "助詞":
            return (morph.base, True)
    return ("", False)

def get_verb(chunk):
    for morph in chunk.morphs:
        if morph.pos == "動詞":
            return (morph.base, True)
    return ("", False)

# Exercise47 expected
def get_expected(chunk):
    length = len(chunk.morphs)
    for idx, morph in enumerate(chunk.morphs):
        if idx > length-2:
            break
        if morph.pos == "名詞" and morph.pos1 == "サ変接続" and chunk.morphs[idx+1].base == "を":
            return (morph.surface + "を", True)
    return ("", False)


def main():
    args = sys.argv

    # Number of command line argments must be 1
    assert len(args) == 3, "Usage: {} in_file out_file".format(args[0])
    in_file = args[1]
    out_file = args[2]

    try:
        open(out_file, "w").close()
    except OSError:
        print("Could not read {} ...".format(out_file))
        sys.exit()

    try:
        fp = open(in_file, "r")
    except OSError:
        print("Could not read {} ...".format(in_file))
        sys.exit()

    chunk_list = make_chunk_list(fp)

    depend_list = list()
    for idx, chunk in enumerate(chunk_list):

        # If chunk is "EOS" then, skip "EOS"
        if chunk == "EOS":
            continue

        srcs = chunk.srcs
        dst  = chunk.dst
        # If there is no destination, then skip the chunk
        if dst == -1:
            continue

        expected_string, result = get_expected(chunk)

        if not result:
            continue

        dst_chunk = find_chunk_by_dst(chunk_list, dst, idx)

        verb, result = get_verb(dst_chunk)
        if result:
            srcs_chunk_list = get_srcs_chunk_list(chunk_list, dst, idx)

            # Remove itself
            srcs_chunk_list = filter(lambda x: x != chunk, srcs_chunk_list)

            postpositional_clause_list = list()
            for srcs_chunk in srcs_chunk_list:
                (postpositional, have_postpositional) = get_postpositional(srcs_chunk)
                if not have_postpositional:
                    continue
                clause = get_chunk_txt(srcs_chunk)
                postpositional_clause_list.append((postpositional, clause))
            # Sort
            postpositional_clause_list = sorted(
                postpositional_clause_list,
                key=lambda x:x[0]
            )

            depend_list.append((expected_string, verb, postpositional_clause_list))

    # Write to file
    for depend in depend_list:
        if not depend[2]: # Empty?
            write_line("{}\n".format(depend[0]+depend[1]), out_file)
        else:
            postpositional_list, clause_list = zip(*depend[2])
            write_line(
                "{}\t{}\t{}\n".format(
                depend[0]+depend[1],
                " ".join(postpositional_list),
                " ".join(clause_list)
                ),
                out_file
            )




if __name__ == "__main__":
    main()
