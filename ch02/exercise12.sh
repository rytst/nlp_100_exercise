#!/bin/bash

#
# Chapter 02
#
# Exercise 12
#

awk '{ print $1 }' popular-names.txt >col1.txt
awk '{ print $2 }' popular-names.txt >col2.txt
