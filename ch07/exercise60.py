#!/usr/bin/python

#
# Chapter 07
#
# Exercise 60
#

from gensim import models


def main():

    try:
        wv = models.KeyedVectors.load_word2vec_format(
            './GoogleNews-vectors-negative300.bin',
            binary=True,
        )
    except:
        print("Could not read file")
        sys.exit()

    print(wv["United_States"])

if __name__ == "__main__":
    main()
