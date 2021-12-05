#! /usr/bin/env python3

def read_input(filename):
    with open(filename) as fd:
        return fd.read().strip()

def compute_result(data):
    horizontal = 0
    depth = 0
    aim = 0
    for item in data:
        if item[0] == "forward":
            horizontal += int(item[1])
            depth += aim * int(item[1])
        elif item[0] == "up":
            aim -= int(item[1])
        elif item[0] == "down":
            aim += int(item[1])
    return abs(horizontal) * abs(depth)

def main():
    data = []
    for line in read_input("input.txt").split("\n"):
        data.append(line.split())
    print(compute_result(data))

if __name__ == '__main__':
    main()
