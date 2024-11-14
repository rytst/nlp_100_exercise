#!/usr/bin/python

#
# Chapter 01
#
# Exercise 02
#

import sys


# Merge strings
def merge_str(str1, str2):
    num_iter = max(len(str1), len(str2))

    output_str = []
    for i in range(num_iter):
        if len(str1) > i:
            output_str.append(str1[i])

        if len(str2) > i:
            output_str.append(str2[i])

    return "".join(output_str)


def main():
    args = sys.argv

    # Number of command line argments must be 2
    if len(args) != 3:
        print("Usage:\n", args[0], "string1", "string2")
        exit(1)

    input_str_1 = args[1]
    input_str_2 = args[2]

    output_str = merge_str(input_str_1, input_str_2)
    print(output_str)


if __name__ == "__main__":
    main()
