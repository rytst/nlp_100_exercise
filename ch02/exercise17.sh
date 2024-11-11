#!/bin/bash

#
# Chapter 02
#
# Exercise 17
#

awk '{ print $1 }' popular-names.txt | sort -d | uniq
