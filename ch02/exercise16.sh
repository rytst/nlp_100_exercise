#!/bin/bash

#
# Chapter 02
#
# Exercise 16
#

usage() {
    echo "Usage: $0 n(number to split)"
    exit 1
}

if [ $# -ne 1 ]; then
    usage
else
    split -n r/$1 popular-names.txt
fi
