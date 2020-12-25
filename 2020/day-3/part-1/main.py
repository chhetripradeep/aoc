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

def calculate(input, width, height):
    x, y = 0, 0
    count = 0
    while x < height:
        if y > width - 1:
            y = y - width
        if input[x][y] == '#':
            count += 1
        x = x + 1
        y = y + 3
        print("x: %d" % x)
        print("y: %d" % y)
    return count

def main():
    input = read_input("input.txt")
    width = len(input[0])
    height = len(input)
    result = calculate(input, width, height)
    print(result)

if __name__ == '__main__':
    main()