#!../venv/bin/python

#
# Chapter 02
#
# Exercise 18
#

import sys
import polars as pl

INPUT_FILE = "popular-names.txt"


def main():

    # Try to read file
    try:
        df = pl.read_csv(INPUT_FILE, separator="\t", has_header=False)
    except OSError:
        print("Could not open/read file:", INPUT_FILE)
        sys.exit()

    # sort by third column
    sorted_df = df.sort(pl.nth(2), descending=True)
    sorted_df.write_csv(sys.stdout, separator='\t', include_header=False)


if __name__ == "__main__":
    main()
