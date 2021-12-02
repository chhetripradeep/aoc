#!/usr/bin/env python3

import sys

def read_input(filename):
    input = []
    with open(filename) as fd:
        lines = fd.readlines()
        for line in lines:
            input.append(int(line.strip()))
    return input

def main():
    input = read_input("input.txt")
    result = 0
    for i in range(0, len(input)-1):
        if input[i] < input[i+1]:
            result += 1
    print(result)

if __name__ == "__main__":
    sys.exit(main())
            