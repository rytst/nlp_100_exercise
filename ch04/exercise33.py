#!/usr/bin/python

#
# Chapter 04
#
# Exercise 33
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

        token_list        = record["line"]
        token_list_length = len(token_list)
        for idx in range(token_list_length):

            # idx: A, idx+1: "の", idx+2: B
            # token_list_length-1: last index
            if idx + 2 > token_list_length - 1:
                break

            first_token  = token_list[idx]
            second_token = token_list[idx+1]
            third_token  = token_list[idx+2]
            if second_token["surface"] != "の":
                continue

            if first_token["pos"] != "名詞" or third_token["pos"] != "名詞":
                continue

            result = first_token["surface"] + second_token["surface"] + third_token["surface"]
            print(result)


if __name__ == "__main__":
    main()
