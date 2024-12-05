#!../venv/bin/python

#
# Chapter 04
#
# Exercise 39
#

import sys
import json
import matplotlib.pyplot as plt


# Dispaly given dictionary data
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

    word_cnt = dict()
    for json_line in json_lines:
        record = json.loads(json_line)

        token_list = record["line"]

        for token in token_list:
            token_pos = token["pos"]
            if (
                token_pos == "空白"
                or token_pos == "助詞"
                or token_pos == "助動詞"
                or token_pos == "補助記号"
            ):
                continue
            token_base = token["base"]

            # Initialization
            if token_base not in word_cnt:
                word_cnt[token_base] = 1
                continue

            word_cnt[token_base] += 1

    sorted_word_cnt = {
        k: v
        for k, v in sorted(word_cnt.items(), key=lambda item: item[1], reverse=True)
    }

    fig = plt.figure()
    data = list(sorted_word_cnt.values())
    order = range(len(data))
    plt.plot(order, data)
    plt.xscale("log", base=10)
    plt.yscale("log", base=10)
    fig.savefig("./figure/exercise39.png")


if __name__ == "__main__":
    main()
