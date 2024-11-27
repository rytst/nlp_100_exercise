#!/usr/bin/python

#
# Chapter 03
#
# Exercise 22
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

    # Extract category name by regular expression
    for line in article.split("\n"):
        results = re.findall(r"^\[\[Category:(.+?)(\|\W*)?\]\]$", line)

        if len(results) > 0:
            print(results[0][0])


if __name__ == "__main__":
    main()
