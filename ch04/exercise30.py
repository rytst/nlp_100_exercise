#!/usr/bin/python

#
# Chapter 04
#
# Exercise 30
#

import sys
import json

# Read text file
def read_text(file_name):
    try:
        f = open(file_name, "r")
    except OSError:
        print("Could not open file: ", file_name)
        sys.exit()

    with f:
        lines = json.load(f)["lines"]

    return lines

# Create mapping
def create_dict(token):

    info_dict = dict()
    info_dict["surface"] = token[0]
    info_dict["base"] = token[3]

    pos_list = token[4].split('-')
    info_dict["pos"]  = pos_list[0]

    if len(pos_list) > 1:
        info_dict["pos1"] = pos_list[1]

    return info_dict

# Generate json record
def gen_record(file_name, output_file):

    try:
        # Initialization
        open(output_file, "w").close()
    except OSError:
        print("Could not open/write file:", output_file)
        sys.exit()


    lines = read_text(file_name)

    new_record = list()
    for line in lines:

        # Skip if there is no token in line (remove "EOS" and "")
        if len(line) < 3:
            new_record = list()
            continue

        for token in line:

            # Skip "EOS" and "" token
            if len(token) < 8:
                continue
            new_record.append(create_dict(token))

        try:
            f = open(output_file, "a")
        except OSError:
            sys.exit()

        with f:
            f.write(
                json.dumps(
                    {"line": new_record},
                    ensure_ascii=False
                ) + '\n'
            )

        new_record = list()




def main():
    args = sys.argv

    # Number of command line argments must be 1
    assert len(args) == 3, "Usage: {} in_file out_file".format(args[0])
    file_name = args[1]
    output_file  = args[2]
    gen_record(file_name, output_file)


if __name__ == "__main__":
    main()
