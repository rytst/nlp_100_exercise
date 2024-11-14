#!/usr/bin/python

#
# Chapter 01
#
# Exercise 09
#

import sys
import random


def typoglycemia(text):
    words = text.split()

    for idx, word in enumerate(words):
        # Process for string whose length is larger than 4
        if len(word) > 4:
            word = list(word)
            sub_word = word[1:-1]

            # Shuffle string
            new_sub_word = random.sample(sub_word, len(sub_word))
            word[1:-1] = new_sub_word
            words[idx] = "".join(word)

    return " ".join(words)


def main():
    args = sys.argv

    # Number of command line argments must be 1
    if len(args) != 2:
        print("Usage:\n", args[0], "text")
        exit(1)

    input_text = args[1]

    output_text = typoglycemia(input_text)
    print(output_text)


if __name__ == "__main__":
    main()
