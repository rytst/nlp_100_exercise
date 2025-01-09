#!/usr/bin/python3

#
# Chapter 07
#
# Exercise 65
#

IN_FILE = "./exercise64.txt"

import sys

def main():

    try:
        f = open(IN_FILE)
    except OSError:
        print("Could not open file: ", IN_FILE)
        sys.exit()

    with f:

        accs = {
            "semantic": {
                "correct": 0,
                "length": 0,
            },
            "syntactic": {
                "correct": 0,
                "length": 0,
            },
        }

        currrent = "" # "semantic" or "syntactic"
        for line in f:
            words = line.split()
            if words[0] == ":":
                if "gram" in line:
                    currrent = "syntactic"
                else:
                    currrent = "semantic"
                continue
            accs[currrent]["length"] += 1
            if words[3] == words[4]:
                accs[currrent]["correct"] += 1

        print("semantic: ",  accs["semantic"]["correct"]  / accs["semantic"]["length"])
        print("syntactic: ", accs["syntactic"]["correct"] / accs["syntactic"]["length"])


if __name__ == "__main__":
    main()
