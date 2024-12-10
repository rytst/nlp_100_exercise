#!/bin/bash

#
# Chapter 05
#
# Exercise 45
#

cat verb_postpositional.txt | sort | uniq -c | sort -n -r -k1
