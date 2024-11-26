#!/usr/bin/python

#
# Chapter 03
#
# Exercise 23
#

import sys
import json
import re


# Get article from json by giving title key
def get_article(title):
    # Open and read json file
    with open("./jawiki-country.json", "r") as json_file:
        json_list = list(json_file)

    # Extract specified data
    for json_recode in json_list:
        recode = json.loads(json_recode)
        if recode["title"] == title:
            return recode["text"]


def main():
    args = sys.argv

    # Number of command line argments must be 1
    assert len(args) == 2, "Usage: {} title".format(args[0])

    title = args[1]

    article = get_article(title)

    assert article is not None, 'Title "{}"is not found.'.format(title)

    for line in article.split("\n"):
        match = re.search(r"^==+\s?\w+\s?==+$", line)  # Space character
        if match:
            section_name = re.search(r"\w+", line)
            section_match_head = re.search(r"^==+", line)
            section_match_tail = re.search(r"==+$", line)

            # Header style syntax check
            assert len(section_match_head.group()) == len(
                section_match_tail.group()
            ), "Header style error"

            # Section level of `== Section ==` is 1
            section_level = len(section_match_head.group()) - 1

            print("------------------------------------")
            print("Section name:  ", section_name.group())
            print("Section level: ", section_level)


if __name__ == "__main__":
    main()
