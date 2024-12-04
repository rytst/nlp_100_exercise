#!/usr/bin/python

#
# Chapter 04
#
# Exercise 33
#

import sys
import json
from collections import deque


def main():
    args = sys.argv

    # Number of command line argments must be 1
    assert len(args) == 2, "Usage: {} file".format(args[0])
    file_name = args[1]

    try:
        fp = open(file_name, "r")
    except OSError:
        print("Could not open/read file:", file_name)
        sys.exit()
    with fp:
        json_lines = list(fp)

    for json_line in json_lines:
        record = json.loads(json_line)

        token_list        = record["line"]
        token_list_length = len(token_list)

        # length of "A の B" must be 3 or more
        if token_list_length < 3:
            continue

        # Initialization for queue
        q = deque()
        q.append(token_list[0])
        q.append(token_list[1])
        for idx in range(token_list_length):

            # idx: A, idx+1: "の", idx+2: B
            # token_list_length-1: last index
            if idx + 2 > token_list_length - 1:
                break

            q.append(token_list[idx+2])
            if q[1]["surface"] != "の":
                continue

            if q[0]["pos"] != "名詞" or q[2]["pos"] != "名詞":
                continue

            result = q[0]["surface"] + q[1]["surface"] + q[2]["surface"]
            print(result)

            q.popleft()


if __name__ == "__main__":
    main()
