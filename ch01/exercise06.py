#!/usr/bin/python

#
# Chapter 01
#
# Exercise 06
#

import sys


def ngram(text, n):

    # n-gram for characters
    length = len(text)

    # process for (length < n)
    if (length < n):
        print("n is larger than the number of characters")
        exit(1)

    num_iter = length - (n - 1)

    ngram_list = []
    for i in range(num_iter):
        elem = ''.join(text[i:i+n])
        ngram_list.append(elem)

    return ngram_list


def main():
    args = sys.argv

    # Number of command line argments must be 3
    if len(args) != 4:
        print("Usage:\n", args[0], "text1", "text2", "bi-gram")
        exit(1)

    text1  = args[1] 
    text2  = args[2]
    bigram = args[3]

    text1_bigram = set(ngram(text=text1, n=2))  # X
    text2_bigram = set(ngram(text=text2, n=2))  # Y

    print("Union: ",        text1_bigram | text2_bigram)
    print("Intersection: ", text1_bigram & text2_bigram)
    print("Difference: ",   text1_bigram - text2_bigram)

    if bigram in text1_bigram:
        print("\"{}\"".format(bigram), "is in X.")
    else:
        print("\"{}\"".format(bigram), "is not in X.")

    if bigram in text2_bigram:
        print("\"{}\"".format(bigram), "is in Y.")
    else:
        print("\"{}\"".format(bigram), "is not in Y.")






if __name__ == "__main__":
    main()
