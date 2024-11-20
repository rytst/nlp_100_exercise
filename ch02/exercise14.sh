#!/bin/bash

#
# Chapter 02
#
# Exercise 14
#

usage() {
    echo "Usage: $0 n(number of lines) filename"
    exit 1
}

if [ $# -ne 2 ]; then
    usage
else
    head -n $1 $2
fi
