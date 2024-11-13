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
    with open("./jawiki-country.json", 'r') as json_file:
        json_list = list(json_file)

    # Extract specified data
    for json_recode in json_list:
        recode = json.loads(json_recode)
        if recode["title"] == title:
            return recode["text"]




def main():
    args = sys.argv

    # Number of command line argments must be 1
    if len(args) != 2:
        print("Usage:\n", args[0], "title")
        exit(1)

    title = args[1]

    article = get_article(title)

    if (article == None):
        print("Title", "\"{}\"".format(title), "is not found.")
        return


    # Extract category name by regular expression
    for line in article.split('\n'):
        match = re.search(r"^\[\[Category:.+\]\]$", line)
        if match:
            category_name = re.sub(r"^\[\[Category:", '', line)
            category_name = re.sub(r"\]\]$", '', category_name)
            category_name = re.search(r"\w+", category_name)

            print(category_name.group())




if __name__ == "__main__":
    main()
