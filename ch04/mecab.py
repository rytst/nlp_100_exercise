#!../venv/bin/python

#
# Chapter 04
#
# Morphological Analysis to `neko.txt`
#

import sys
import json
import MeCab

INPUT_FILE = "./neko.txt"
OUTPUT_FILE = "./neko.txt.mecab"

try:
    f = open(INPUT_FILE, "r")
except OSError:
    sys.exit()

with f:
    contents = f.readlines()

data = dict()
data["lines"] = list()
for content in contents:
    wakati = MeCab.Tagger("-Owakati")
    tagger = MeCab.Tagger()
    tokens = tagger.parse(content)

    line_info = list()
    for token in tokens.split("\n"):
        line_info.append(token.split("\t"))

    data["lines"].append(line_info)

try:
    f = open(OUTPUT_FILE, "w")
except OSError:
    sys.exit()

with f:
    json.dump(data, f, ensure_ascii=False, indent=2)
