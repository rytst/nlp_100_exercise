#!/bin/python


import sys

def main():

    args = sys.argv

    assert len(args) == 2, "Invlid command line args"

    file_name = args[1]

    try:
        fp = open(file_name, "r")
    except OSError:
        print("Could not open file ...")
        sys.exit()

    with fp:
        n = 0
        l = 0
        p = 0
        for line in fp.read().splitlines():
            n += line.index("N") + 1
            l += line.index("L") + 1
            p += line.index("P") + 1
    print(1 * n + 2 * l + 3 * p)



if __name__ == "__main__":
    main()
