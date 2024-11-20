#!../venv/bin/python

#
# Chapter 02
#
# Exercise 13
#

import sys
import polars as pl

INPUT_FILES = ["col1.txt", "col2.txt"]
OUTPUT_FILE = "merged.txt"


def main():

    # Initialization DataFrame
    df_left = pl.DataFrame({})

    for i in range(2):
        try:
            df_right = pl.read_csv(INPUT_FILES[i], separator="\t")
        except OSError:
            print("Could not open/read file:", INPUT_FILES[i])
            sys.exit()

        df_left = df_left.with_columns(df_right)

    try:
        open(OUTPUT_FILE, "w")
    except OSError:
        print("Could not open/write file:", OUTPUT_FILE)

    # Write data to OUTPUT_FILE
    df_left.write_csv(OUTPUT_FILE, separator="\t")


if __name__ == "__main__":
    main()
