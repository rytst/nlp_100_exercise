#!../venv/bin/python

#
# Chapter 02
#
# Exercise 12
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

    for i in range(2):
        col = df.select(pl.nth(i))

        # col1.txt and col2.txt
        OUTPUT_FILE = "col{}.txt".format(i + 1)

        try:
            open(OUTPUT_FILE, "w")
        except OSError:
            print("Could not open/write file:", OUTPUT_FILE)

        # Write data to OUTPUT_FILE
        col.write_csv(OUTPUT_FILE, include_header=False)


if __name__ == "__main__":
    main()
