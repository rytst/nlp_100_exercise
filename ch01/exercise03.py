#!/usr/bin/python

#
# Chapter 01
#
# Exercise 00
#

import sys


def text_to_list(text):
    words = text.split()

    # Uppercase range
    upper_first = ord('A')
    upper_last  = ord('Z')

    # Lowercase range
    lower_first = ord('a')
    lower_last  = ord('z')

    output_list = []
    for word in words:

        char_count = 0
        for char in word:

            is_upper = upper_first <= ord(char) and ord(char) <= upper_last
            is_lower = lower_first <= ord(char) and ord(char) <= lower_last

            if is_upper or is_lower:
                char_count += 1

        output_list.append(char_count)


    return output_list


def main():
    args = sys.argv

    # Number of command line argments must be 1
    if len(args) != 2:
        print("Usage:\n", args[0], "text")
        exit(1)

    text = args[1] 

    output_list = text_to_list(text)
    print(output_list)




if __name__ == "__main__":
    main()
