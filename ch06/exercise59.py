#!../venv/bin/python

#
# Chapter 06
#
# Exercise 59
#

import polars as pl
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import optuna

TRAIN_FILE = "./data/train.feature.txt"
VALID_FILE = "./data/valid.feature.txt"
TEST_FILE  = "./data/test.feature.txt"


def objective(trial):
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



    # Label Encoding
    for label, idx in zip(list(enc.inverse_transform([0,1,2,3])), [0,1,2,3]):
        print(label, ":", idx)

    solver = trial.suggest_categorical("solver", ["lbfgs", "newton-cg", "sag", "saga"])
    C = trial.suggest_float("C", 1e-5, 1e5, log=True)
    clf = LogisticRegression(C=C, solver=solver, n_jobs=5)

    clf.fit(train, y_train)
    score = clf.score(valid, y_valid)
    return score


def main():
    study = optuna.create_study(direction="maximize")
    study.optimize(objective, n_trials=20)
    print(study.best_trial)
    try:
        test  = pl.read_csv(
            TEST_FILE,
            has_header=True,
            quote_char=None,
            separator="\t"
        )
    except:
        print("Could not read {} ...".format(file_name))
        sys.exit()

    y_test = test.select(
        pl.col("CATEGORY")
        .map_batches(enc.transform)
    )
    test  = test.drop(["URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"])



if __name__ == "__main__":
    main()
