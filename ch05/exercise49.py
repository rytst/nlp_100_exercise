#!/usr/bin/python

#
# Chapter 05
#
# Exercise 49
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

def get_chunk_txt_rep_noun(chunk, noun):
    txt = ""
    first_noun = True
    for morph in chunk.morphs:
        if morph.pos == "記号":
            continue
        if first_noun:
            if morph.pos == "名詞":
                txt += noun
                first_noun = False
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

def get_noun_chunk(chunk_list, idx):
    i = 1
    noun_list = list()
    while True:
        chunk = chunk_list[idx+i]
        if chunk == "EOS":
            break
        if have_pos(chunk, "名詞"):
            noun_list.append(chunk)
        i += 1
    return noun_list


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

def path_i_to_j(x_chunk, y_chunk, chunk_list, idx):

    target = y_chunk.srcs

    srcs = x_chunk.srcs
    dst  = x_chunk.dst

    result = get_chunk_txt_rep_noun(x_chunk, "X")
    if dst == target:
        return result + "->" + get_chunk_txt_rep_noun(y_chunk, "Y")

    while True:
        next_chunk = find_chunk_by_dst(chunk_list, dst, idx)
        srcs = next_chunk.srcs 
        dst  = next_chunk.dst
        if dst == target:
            return result + "->" + get_chunk_txt_rep_noun(y_chunk, "Y")
        result += "->" + get_chunk_txt(next_chunk)

def i_to_j_exist(x_chunk, y_chunk, chunk_list, idx):

    if x_chunk.dst == -1:
        return False

    j = y_chunk.srcs

    if x_chunk.dst == j:
        return True

    dst_chunk = find_chunk_by_dst(chunk_list, x_chunk.dst, idx)
    return i_to_j_exist(dst_chunk, y_chunk, chunk_list, idx)

def i_and_j_common_exist(x_chunk, y_chunk, chunk_list, idx):

    x_path = list() 
    y_path = list()

    x_flag = False
    y_flag = False
    while True:
        if x_chunk.dst == -1:
            x_flag = True
        if y_chunk.dst == -1:
            y_flag = True

        if not x_flag:
            x_chunk = find_chunk_by_dst(chunk_list, x_chunk.dst, idx)
            x_path.append(x_chunk.srcs)

        if not y_flag:
            y_chunk = find_chunk_by_dst(chunk_list, y_chunk.dst, idx)
            y_path.append(y_chunk.srcs)

        common = sorted(list(set(x_path).intersection(y_path)))

        if common:
            return common
        if x_flag and y_flag:
            return list()


def path_i_and_j(x_chunk, y_chunk, chunk_list, idx, common):

    x_srcs = x_chunk.srcs
    x_dst  = x_chunk.dst

    y_srcs = y_chunk.srcs
    y_dst  = y_chunk.dst

    first_x = get_chunk_txt_rep_noun(x_chunk, "X")
    first_y = get_chunk_txt_rep_noun(y_chunk, "Y")

    x_path_list = list()
    y_path_list = list()
    x_path_list.append(first_x)
    y_path_list.append(first_y)

    x_flag = False
    y_flag = False

    while True:
        if x_srcs != common:
            x_chunk = find_chunk_by_dst(chunk_list, x_chunk.dst, idx)
            x_path_list.append(get_chunk_txt(x_chunk))
            x_srcs = x_chunk.srcs
            x_dst  = x_chunk.dst
        else:
            x_flag = True
        if y_srcs != common:
            y_chunk = find_chunk_by_dst(chunk_list, y_chunk.dst, idx)
            y_path_list.append(get_chunk_txt(y_chunk))
            y_srcs = y_chunk.srcs
            y_dst  = y_chunk.dst
        else:
            y_flag = True

        if x_flag and y_flag:
            break

    x_path_list = x_path_list[:-1]
    y_path_list = y_path_list[:-1]
    last_list = list()
    last_list.append(get_chunk_txt(x_chunk))
    while True:
        if x_dst == -1:
            break

        x_chunk = find_chunk_by_dst(chunk_list, x_chunk.dst, idx)
        last_list.append(get_chunk_txt(x_chunk))
        x_srcs = x_chunk.srcs
        x_dst  = x_chunk.dst
    return x_path_list, y_path_list, last_list

def list_to_string(x_path_list, y_path_list, last_list):

    result = ""
    for x_path in x_path_list:
        result += x_path + "->"

    result = result[:-2]
    result += "|"

    for y_path in y_path_list:
        result += y_path + "->"

    result = result[:-2]
    result += "|"

    for path in last_list:
        result += path + "->"

    result = result[:-2]
    return result



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

        x_chunk = chunk

        noun_list = get_noun_chunk(chunk_list, idx)
        if len(noun_list) < 1:
            continue

        for y_chunk in noun_list:
            common = i_and_j_common_exist(x_chunk, y_chunk, chunk_list, idx)
            if common:
                x_path_list, y_path_list, last_list = path_i_and_j(x_chunk, y_chunk, chunk_list, idx, common[0])
                path = list_to_string(x_path_list, y_path_list, last_list)
                print(path)

            elif i_to_j_exist(x_chunk, y_chunk, chunk_list, idx):
                #print(get_chunk_txt(x_chunk), get_chunk_txt(y_chunk))
                path = path_i_to_j(x_chunk, y_chunk, chunk_list, idx)
                print(path)




if __name__ == "__main__":
    main()
