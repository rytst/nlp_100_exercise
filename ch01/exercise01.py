#!/usr/bin/python

#
# Chapter 01
#
# Exercise 01
#


def extract_str(input_str):
    length = len(input_str)

    output_length = int(length / 2)
    output_str = []
    for i in range(output_length):
        output_str.append(input_str[2 * i])

    return "".join(output_str)


def main():
    merged_str = "パタトクカシーー"

    output_str = extract_str(merged_str)
    print(output_str)


if __name__ == "__main__":
    main()
