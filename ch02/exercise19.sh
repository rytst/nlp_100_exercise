#!/bin/bash

#
# Chapter 02
#
# Exercise 19
#

awk '{ print $1 }' popular-names.txt | sort -d | uniq -c | sort -n -r -k 1
