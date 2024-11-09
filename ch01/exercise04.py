#!/usr/bin/python

#
# Chapter 01
#
# Exercise 00
#

import sys


def text_to_dict(text, index_list):
    words = text.split()

    # Uppercase range
    upper_first = ord('A')
    upper_last  = ord('Z')

    # Lowercase range
    lower_first = ord('a')
    lower_last  = ord('z')

    output_dict = dict()
    for idx, word in enumerate(words):

        if idx+1 in index_list:
            output_dict[word[0]] = idx + 1

        else:
            output_dict[word[0:2]] = idx + 1

        # for char in word:

        #     is_upper = upper_first <= ord(char) and ord(char) <= upper_last
        #     is_lower = lower_first <= ord(char) and ord(char) <= lower_last

        #     if is_upper or is_lower:
        #         char_count += 1

        # output_list.append(char_count)


    return output_dict


def main():
    args = sys.argv

    # Number of command line argments must be 1
    if len(args) != 2:
        print("Usage:\n", args[0], "text")
        return

    text = args[1] 

    index_list = [1, 5, 6, 7, 8, 9, 15, 19]
    output_dict = text_to_dict(text, index_list)
    print(output_dict)




if __name__ == "__main__":
    main()
