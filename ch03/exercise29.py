#!../venv/bin/python

#
# Chapter 03
#
# Exercise 29
#

import sys
import json
import re
import requests


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
        result[splitted[0][0].strip()] = splitted[0][1].strip()  # remove space

    return result


def im_name_to_url(image_name):
    S = requests.Session()

    # API
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": "File:{}".format(image_name),
        "iiprop": "url",
    }
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    data = DATA["query"]["pages"]

    key, value = next(iter(data.items()))  # Get first item

    return value["imageinfo"][0]["url"]


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
    result = create_dict(basic_info)

    try:
        image_name = result["国旗画像"]
    except KeyError:
        print("Key is not found.")
        sys.exit()

    url = im_name_to_url(image_name)
    print(url)


if __name__ == "__main__":
    main()
