#!../venv/bin/python

#
# Chapter 06
#
# Exercise 52 53
#

import polars as pl
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix

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

    for label, idx in zip(list(enc.inverse_transform([0,1,2,3])), [0,1,2,3]):
        print(label, ":", idx)
    clf = LogisticRegression(random_state=42)

    # Exercise52
    clf.fit(train, y_train)

    # Exercise53
    pred_proba = clf.predict_proba(train)
    preds       = clf.predict(train)
    probas     = np.max(pred_proba, axis=1)
    print(preds)

    for pred, proba in zip(preds, probas):
        print(enc.inverse_transform([pred])[0], ":", proba)


    # Exercise54
    print("Training data:", clf.score(train, y_train))
    print("Test data:", clf.score(test, y_test))

    # Exercise55
    pred = clf.predict(test)
    print("Confusion Matrix")
    print(confusion_matrix(y_test, pred))


if __name__ == "__main__":
    main()
