#!/usr/bin/python

#
# Chapter 04
#
# Exercise 31
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

        for token in record["line"]:

            # extract "動詞"
            if token["pos"] == "動詞":
                print(token["surface"])


if __name__ == "__main__":
    main()
