#!../venv/bin/python

#
# Chapter 06
#
# Exercise 58
#

import polars as pl
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

TRAIN_FILE = "./data/train.feature.txt"
VALID_FILE = "./data/valid.feature.txt"
TEST_FILE  = "./data/test.feature.txt"


def main():
    try:
        train = pl.read_csv(
            TRAIN_FILE,
            has_header=True,
            quote_char=None,
            separator="\t"
        )
        valid = pl.read_csv(
            VALID_FILE,
            has_header=True,
            quote_char=None,
            separator="\t"
        )
        test  = pl.read_csv(
            TEST_FILE,
            has_header=True,
            quote_char=None,
            separator="\t"
        )
    except:
        print("Could not read {} ...".format(file_name))
        sys.exit()

    enc = LabelEncoder()
    enc.fit(["e", "b", "m", "t"])
    y_train = train.select(
        pl.col("CATEGORY")
        .map_batches(enc.transform)
    )
    train = train.drop(["URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"])

    y_valid = valid.select(
        pl.col("CATEGORY")
        .map_batches(enc.transform)
    )
    valid = valid.drop(["URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"])

    y_test = test.select(
        pl.col("CATEGORY")
        .map_batches(enc.transform)
    )
    test  = test.drop(["URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"])

    # Label Encoding
    for label, idx in zip(list(enc.inverse_transform([0,1,2,3])), [0,1,2,3]):
        print(label, ":", idx)


    c_params = np.arange(start=1e-8, stop=10, step=1)
    train_scores = list()
    valid_scores = list()
    test_scores  = list()
    for c in tqdm(c_params):
        clf = LogisticRegression(C=c, random_state=42)
        clf.fit(train, y_train)

        train_score = clf.score(train, y_train)
        train_scores.append(train_score)

        valid_score = clf.score(valid, y_valid)
        valid_scores.append(valid_score)

        test_score  = clf.score(test,  y_test)
        test_scores.append(test_score)

    plt.plot(c_params, train_scores)
    plt.savefig("./image/train.png")
    plt.clf()
    plt.plot(c_params, valid_scores)
    plt.savefig("./image/valid.png")
    plt.clf()
    plt.plot(c_params, test_scores)
    plt.savefig("./image/test.png")
    plt.clf()


if __name__ == "__main__":
    main()
