#!/usr/bin/python3

#
# Chapter 07
#
# Exercise 66
#

IN_FILE = "./combined.csv"

from gensim import models
import numpy as np
import sys
from tqdm import tqdm
import polars as pl
from scipy.stats import spearmanr

def main():

    try:
        wv = models.KeyedVectors.load_word2vec_format(
            './GoogleNews-vectors-negative300.bin',
            binary=True,
        )
    except:
        print("Could not read file")
        sys.exit()

    combined = pl.read_csv(IN_FILE, has_header=True)
    new_column = combined.map_rows(
        lambda row: wv.similarity(row[0], row[1]),
        return_dtype=pl.Float64,
    )
    corr, p = spearmanr(new_column, combined.select("Human (mean)"))
    print(f"Corr: {corr}")
    print(f"P: {p}")



if __name__ == "__main__":
    main()
