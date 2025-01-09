#!/usr/bin/python3

#
# Chapter 07
#
# Exercise 66
#

IN_FILE = "./countries_of_the_world.csv"

from gensim import models
import numpy as np
import sys
from tqdm import tqdm
import polars as pl
from scipy.stats import spearmanr
from sklearn.cluster import KMeans

def get_vec(wv, name):
    try:
        vec = wv[name]
        print(vec)
        return vec
    except:
        return None


def main():

    try:
        wv = models.KeyedVectors.load_word2vec_format(
            './GoogleNews-vectors-negative300.bin',
            binary=True,
        )
    except:
        print("Could not read file")
        sys.exit()

    countries = pl.Series(
        pl.read_csv(IN_FILE, has_header=True).select(
            pl.col("Country").str.strip_chars().str.replace(" ", "_").str.replace("'", "")
        )
    ).to_list()

    data = {
        "countries": list(),
        "vecs": list()
    }

    for country in countries:
        try:
            data["vecs"].append(
                np.array(wv.get_vector(country),"float64")
            )
            data["countries"].append(country)
        except:
            pass
    print(data)
    pred = KMeans(n_clusters = 5).fit_predict(np.array(data["vecs"]).reshape(-1, 1))
    for zone, name in zip(pred, data["countries"]):
        print("------------------------")
        print("Zone: ", zone)
        print("country: ", name)

if __name__ == "__main__":
    main()

# Corr: 0.7000166486272194
# P: 2.86866666051422e-53
