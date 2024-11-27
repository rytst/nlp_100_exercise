#!/usr/bin/python

#
# Chapter 03
#
# Exercise 26
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


# Basic information to dictionary
def create_dict(basic_info):
    result = dict()
    for line in basic_info.split("\n"):
        splitted = re.findall(r"\|(.+)=(.+)", line)

        # Skip `{{基礎情報 国` and `}}`
        if len(splitted) == 0:
            continue

        # splitted[0][1:]
        # "|key" -> "key"
        result[splitted[0][0].strip()] = splitted[0][1].strip()

    return result


def rm_emphasis(basic_info):
    removed = re.sub(r"'{2,3}|'{5}", "", basic_info)
    return removed


# Print dictionary
def print_result(result):
    for key, value in result.items():
        print(key, ":", value)


def main():
    args = sys.argv

    # Number of command line argments must be 1
    assert len(args) == 2, "Usage: {} title".format(args[0])

    title = args[1]

    article = get_article(title)

    assert article is not None, 'Title "{}"is not found.'.format(title)

    """
    {{基礎情報 国
    |key0 = value0
    |key1 = value1
    |key2 = value2
          :
          :
    |keyn = valuen
    }}
    """
    match = re.search(r"\{\{基礎情報\s\w+\n(.+\n)*}}", article)

    assert match is not None, "Basic information is not found."

    basic_info = match.group()
    basic_info = rm_emphasis(basic_info)
    result = create_dict(basic_info)
    print_result(result)


if __name__ == "__main__":
    main()
