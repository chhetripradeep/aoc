#!/usr/bin/env python3

import sys

def read_input(filename):
    input = []
    with open(filename) as fd:
        lines = fd.readlines()
        for line in lines:
            input.append(int(line))
    return input

def calculate(input):
    length = len(input)
    for i in range(0, length):
        for j in range(i, length):
            if input[i] + input[j] == 2020:
                return input[i] * input[j] 

def main():
    input = read_input("input.txt")
    result = calculate(input)
    print(result)

if __name__ == '__main__':
    sys.exit(main())
