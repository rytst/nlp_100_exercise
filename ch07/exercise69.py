#!/usr/bin/python3

#
# Chapter 07
#
# Exercise 69
#

IN_FILE = "./countries_of_the_world.csv"

from gensim import models
import numpy as np
import sys
from tqdm import tqdm
import polars as pl
from scipy.stats import spearmanr
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

figure(figsize=(16, 4), dpi=1024)

def get_vec(wv, name):
    try:
        vec = wv[name]
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
    label = KMeans(n_clusters = 5).fit_predict(np.array(data["vecs"]).reshape(-1, 1))
    for zone, country in zip(label, data["countries"]):
        print("------------------------")
        print("Zone: ", zone)
        print("country: ", country)

    dendro = dendrogram(linkage(data["vecs"], method="ward"), labels=data["countries"])
    plt.savefig("./dendro.png", format="png")

if __name__ == "__main__":
    main()
