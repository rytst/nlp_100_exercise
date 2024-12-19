#!../venv/bin/python

#
# Chapter 06
#
# Exercise 52 53 54 55 56
#

import polars as pl
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report

TRAIN_FILE = "./data/train.feature.txt"
VALID_FILE = "./data/valid.feature.txt"
TEST_FILE  = "./data/test.feature.txt"

def wall():
    print("=====================================================================")

def line():
    print("---------------------------------------------------------------------")

def show_top10(coef, enc, train):
    train.columns
    for idx, label in enumerate(enc.inverse_transform([0,1,2,3])):
        print("top10 of", label)
        top10_name = np.array(train.columns)[np.argsort(coef[idx])[::-1]][:10]
        top10      = np.sort(coef[idx])[::-1][:10]
        for name, val in zip(top10_name, top10):
            print(name, ":", val)
        line()



def show_bottom10(coef, enc, train):
    train.columns
    for idx, label in enumerate(enc.inverse_transform([0,1,2,3])):
        print("top10 of", label)
        top10_name = np.array(train.columns)[np.argsort(coef[idx])][:10]
        top10      = np.sort(coef[idx])[:10]
        for name, val in zip(top10_name, top10):
            print(name, ":", val)
        line()


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
    clf = LogisticRegression(random_state=42)

    # Exercise52
    clf.fit(train, y_train)
    wall()

    # Exercise53
    pred_proba = clf.predict_proba(train)
    preds       = clf.predict(train)
    probas     = np.max(pred_proba, axis=1)
    print(preds)

    for pred, proba in zip(preds, probas):
        print(enc.inverse_transform([pred])[0], ":", proba)

    wall()


    # Exercise54
    print("Training data:", clf.score(train, y_train))
    print("Test data:", clf.score(test, y_test))
    wall()

    # Exercise55
    pred = clf.predict(test)
    print("Confusion Matrix")
    print(confusion_matrix(y_test, pred))
    wall()

    # Exercise56
    report = classification_report(y_test, pred)
    print(report)
    wall()

    # Exercise57
    coef = clf.coef_
    show_top10(coef, enc, train)
    wall()
    show_bottom10(coef, enc, train)
    wall()


if __name__ == "__main__":
    main()
