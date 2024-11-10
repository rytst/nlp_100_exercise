#!/usr/bin/python

#
# Chapter 01
#
# Exercise 00
#

import sys


def ngram(text, n, method):

    # n-gram for words
    if method == "word":
        words = text.split()

        length = len(words)
        num_iter = length - (n - 1)

        ngram_list = []
        for i in range(num_iter):
            elem = ' '.join(words[i:i+n])
            ngram_list.append(elem)

        return ngram_list

    # n-gram for characters
    elif method == "char":

        length   = len(text)
        num_iter = length - (n - 1)

        ngram_list = []
        for i in range(num_iter):
            elem = ''.join(text[i:i+n])
            ngram_list.append(elem)

        return ngram_list

    else:
        print("method parameter is invalid")
        exit(1)


def main():
    args = sys.argv

    # Number of command line argments must be 3
    if len(args) != 4:
        print("Usage:\n", args[0], "text", "n", "method")
        exit(1)

    text   = args[1] 
    n      = int(args[2])
    method = args[3]

    output_ngram = ngram(text=text, n=n, method=method)
    print(output_ngram)




if __name__ == "__main__":
    main()
