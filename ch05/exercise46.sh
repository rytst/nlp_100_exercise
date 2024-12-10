#!/bin/bash

#
# Chapter 05
#
# Exercise 46
#

cat verb_postpositional.txt | sort | uniq -c | sort -n -r -k1 | grep -E $'\s行う\t|\sなる\t|\s与える\t'
