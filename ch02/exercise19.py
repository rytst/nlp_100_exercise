#!../venv/bin/python

#
# Chapter 02
#
# Exercise 19
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

    first_col = df.select(pl.nth(0))
    col_name = first_col.to_series().name
    out_df = (
        first_col.group_by(col_name)  # Unique name
        .len()
        .sort(pl.nth(1), descending=True)
    ).select(pl.nth(0))

    # Print output
    out_df.write_csv(sys.stdout, include_header=False)


if __name__ == "__main__":
    main()
