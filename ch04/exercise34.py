#!/usr/bin/python

#
# Chapter 04
#
# Exercise 34
#

import sys
import json


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

        token_list = record["line"]

        seq = list()
        for token in token_list:
            if token["pos"] == "名詞":
                seq.append(token["surface"])
                continue

            if len(seq) > 0:
                print("".join(seq))
                seq = list()

        if len(seq) > 0:
            print("".join(seq))


if __name__ == "__main__":
    main()
