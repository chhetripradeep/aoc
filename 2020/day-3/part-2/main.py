#!/usr/bin/env python3

def read_input(filepath):
    input = []
    with open(filepath) as fd:
        lines = fd.readlines()
        for line in lines:
            line = line.strip()
            char_arr = []
            for character in line:
                char_arr.append(character)
            input.append(char_arr)
    return input

def calculate(input, right, down):
    width = len(input[0])
    height = len(input)
    x, y = 0, 0
    count = 0
    while x < height:
        if y > width - 1:
            y = y - width
        if input[x][y] == '#':
            count += 1
        x = x + down
        y = y + right
    return count

def main():
    input = read_input("input.txt")
    right_downs = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    result = 1
    for rd in right_downs:
        result = result * calculate(input, rd[0], rd[1])
    print(result)

if __name__ == '__main__':
    main()