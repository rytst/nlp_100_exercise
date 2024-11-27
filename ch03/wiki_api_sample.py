#This file is auto-generated. See modules.json and autogenerator.py for details
# https://en.wikipedia.org/w/api.php?action=query&format=json&prop=imageinfo&titles=File%3ARoyal_Coat_of_Arms_of_the_United_Kingdom.svg&formatversion=2&iiprop=url

#!/usr/bin/python3

"""
    get_imageinfo.py

    MediaWiki API Demos
    Demo of `Imageinfo` module: Get information about an image file.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    #"titles": "File:Flag of Japan.svg",
    "titles": "File:Flag of the United Kingdom.svg",
    "iiprop": "url"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    print(v["imageinfo"][0]["url"])


