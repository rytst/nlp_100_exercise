#!/usr/bin/python

#
# Chapter 01
#
# Exercise 04
#

import sys


def text_to_dict(text, index_list):
    words = text.split()

    output_dict = dict()
    for idx, word in enumerate(words):

        if idx+1 in index_list:
            output_dict[word[0]] = idx + 1

        else:
            output_dict[word[0:2]] = idx + 1

    return output_dict


def main():
    args = sys.argv

    # Number of command line argments must be 1
    if len(args) != 2:
        print("Usage:\n", args[0], "text")
        exit(1)

    text = args[1] 

    index_list = [1, 5, 6, 7, 8, 9, 15, 19]
    output_dict = text_to_dict(text, index_list)
    print(output_dict)




if __name__ == "__main__":
    main()
