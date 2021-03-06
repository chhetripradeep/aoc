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
    down = 1
    right = 3
    input = read_input("input.txt")
    result = calculate(input, right, down)
    print(result)

if __name__ == '__main__':
    main()