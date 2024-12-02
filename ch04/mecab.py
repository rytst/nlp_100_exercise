#!../venv/bin/python

#
# Chapter 04
#
# Morphological Analysis to `neko.txt`
#

import sys
import MeCab

INPUT_FILE  = "./neko.txt"
OUTPUT_FILE = "./neko.txt.mecab"

try:
    f = open(INPUT_FILE, "r")
except OSError:
    sys.exit()

with f:
    contents = f.read()

wakati = MeCab.Tagger("-Owakati")
tagger = MeCab.Tagger()
new_contents = tagger.parse(contents)

try:
    f = open(OUTPUT_FILE, "w")
except OSError:
    sys.exit()

with f:
    f.write(new_contents)
