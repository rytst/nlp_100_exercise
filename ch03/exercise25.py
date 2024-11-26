#!/usr/bin/python

#
# Chapter 03
#
# Exercise 25
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
    match = re.search(r"\{\{基礎情報\s\w+\n(\|.+\n)*}}", article)

    assert match is not None, "Basic information is not found."

    basic_info = match.group()

    result = dict()
    for line in basic_info.split("\n"):
        match = re.search(r"=", line)
        if match:
            splitted  = re.split(r"=", line)

            # splitted[0][1:]
            # "|key" -> key
            result[splitted[0][1:]] = splitted[1]

    for key, value in result.items():
        print(key,":", value)


if __name__ == "__main__":
    main()
