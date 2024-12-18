#!../venv/bin/python

#
# Chapter 06
#
# Exercise 50
#

import sys
import polars as pl
from sklearn.model_selection import train_test_split

def rename_header(df, column_names):
    header_dict = dict()
    for idx, column_name in enumerate(column_names):
        original = "column_" + str(idx+1)
        header_dict[original] = column_name
    return df.rename(header_dict)

def main():
    args = sys.argv

    # Number of command line argments must be 1
    assert len(args) == 2, "Usage: {} file".format(args[0])
    file_name = args[1]

    try:
        df = pl.read_csv(
            file_name,
            has_header=False,
            quote_char=None,
            separator="\t"
        )
    except:
        print("Could not read {} ...".format(file_name))
        sys.exit()

    # ID \t TITLE \t URL \t PUBLISHER \t CATEGORY \t STORY \t HOSTNAME \t TIMESTAMP
    column_names = ["id", "title", "url", "publisher", "category", "story", "hostname", "timestamp"]
    df = rename_header(df, column_names)
    df = df.filter(
        pl.col("publisher").is_in(
            [
                "Reuters",
                "Huffington Post",
                "Businessweek",
                "Contactmusic.com",
                "Daily Mail"
            ]
        )
    ).select(pl.col("category"), pl.col("title"))

    train, valid_test = train_test_split(
        df,
        test_size=0.2,
        random_state=42,
    )

    valid, test = train_test_split(
        valid_test,
        test_size=0.5,
        random_state=42,
    )

    print(train)
    print(valid)
    print(test)

    try:
        train.write_csv("./data/train.txt", separator="\t")
        print("train: {}".format(train.height))
        valid.write_csv("./data/valid.txt", separator="\t")
        print("valid: {}".format(valid.height))
        test.write_csv("./data/test.txt",   separator="\t")
        print("test:  {}".format(test.height))
    except:
        print("Could not write ...")
        sys.exit()

if __name__ == "__main__":
    main()
