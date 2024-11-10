#!/bin/bash

#
# Chapter 02
#
# Exercise 14
#

usage() {
    echo "Usage: $0 n(number of lines)"
    exit 1
}

if [ $# -ne 1 ]; then
    usage
else
    head -n $1 popular-names.txt
fi
