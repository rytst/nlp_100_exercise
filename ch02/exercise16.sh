#!/bin/bash

#
# Chapter 02
#
# Exercise 16
#

usage() {
    echo "Usage: $0 n(number to split) filename(to split)"
    exit 1
}

if [ $# -ne 2 ]; then
    usage
else
    split -n r/$1 $2
fi
