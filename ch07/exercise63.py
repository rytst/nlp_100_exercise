#!/usr/bin/python

#
# Chapter 07
#
# Exercise 63
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


    # vec_spain, vec_madrid, vec_athens = wv.get_vector("Spain", norm=True), wv.get_vector("Madrid", norm=True), wv.get_vector("Athens", norm=True)
    # result = wv.similar_by_vector(vec_spain - vec_madrid + vec_athens)[:10]

    result = wv.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'])
    print(result)

if __name__ == "__main__":
    main()
