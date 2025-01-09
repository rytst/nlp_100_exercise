#!/usr/bin/python

#
# Chapter 07
#
# Exercise 61
#

from gensim import models
# from sklearn.metrics.pairwise import cosine_similarity
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

    United_States = np.expand_dims(wv["United_States"], axis=0)
    US = np.expand_dims(wv["U.S."], axis=0)

    res = cosine_similarity(United_States, US)
    print(res[0][0])
#     res = wv.similarity("United_States", "U.S.")
#     print(res)


if __name__ == "__main__":
    main()
