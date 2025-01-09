#!/usr/bin/python

#
# Chapter 07
#
# Exercise 62
#

from gensim import models
import numpy as np

def main():

    try:
        wv = models.KeyedVectors.load_word2vec_format(
            './GoogleNews-vectors-negative300.bin',
            binary=True,
        )
    except:
        print("Could not read file")
        sys.exit()

    res = wv.most_similar(positive=["United_States"])
    print(res)


if __name__ == "__main__":
    main()
