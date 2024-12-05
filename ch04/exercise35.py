#!/usr/bin/python

#
# Chapter 04
#
# Exercise 35
#

import sys
import json


def print_dict(arg_dict):
    for k, v in arg_dict.items():
        print(k, ":", v)


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

    # word_cnt: word_cnt["word"] = count
    word_cnt = dict()
    for json_line in json_lines:
        record = json.loads(json_line)

        token_list = record["line"]

        for token in token_list:

            # Skip unused token
            token_pos = token["pos"]
            if (
                token_pos == "空白"
                or token_pos == "助詞"
                or token_pos == "助動詞"
                or token_pos == "補助記号"
            ):
                continue

            token_base = token["base"]

            # If the key is not found, then add the key to dictionary
            if token_base not in word_cnt:
                word_cnt[token_base] = 0

            word_cnt[token_base] += 1

    # Sort by value
    sorted_word_cnt = {
        k: v
        for k, v in sorted(word_cnt.items(), key=lambda item: item[1], reverse=True)
    }
    print_dict(sorted_word_cnt)


if __name__ == "__main__":
    main()
