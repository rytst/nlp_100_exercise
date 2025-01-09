#!/usr/bin/python3

#
# Chapter 07
#
# Exercise 64
#

IN_FILE = "./questions-words.txt"
OUT_FILE = "./exercise64.txt"

from gensim import models
import numpy as np
import sys
from tqdm import tqdm

def main():

    try:
        wv = models.KeyedVectors.load_word2vec_format(
            './GoogleNews-vectors-negative300.bin',
            binary=True,
        )
    except:
        print("Could not read file")
        sys.exit()

    try:
        # Initialization
        open(OUT_FILE, "w").close()
    except OSError:
        print("Could not open/write file:", OUT_FILE)
        sys.exit()


    try:
        f = open(IN_FILE)
    except OSError:
        print("Could not open file: ", IN_FILE)
        sys.exit()

    try:
        g = open(OUT_FILE, "a")
    except OSError:
        print("Could not open file: ", OUT_FILE)
        sys.exit()

    with f and g:
        for line in tqdm(f):
            words = line.split()
            if words[0] == ":":
                g.write(line)
                continue
            res = wv.most_similar(positive=[words[1], words[2]], negative=[words[0]])[0]
            out_line = line.strip() + f" {res[0]} {res[1]}\n"
            g.write(out_line)

if __name__ == "__main__":
    main()
