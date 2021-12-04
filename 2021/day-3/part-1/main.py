#! /usr/bin/env python3

def read_input(filename):
    with open(filename) as fd:
        return fd.read().strip().split('\n')

def compute_gamma_epsilon(data):
    gamma = ''
    epsilon = ''
    for i in range(len(data[0])):
        count_zero = 0
        count_one = 0
        for j in range(len(data)):
            if data[j][i] == '0':
                count_zero += 1
            else:
                count_one += 1
        if count_zero > count_one:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return gamma, epsilon

def bin2dec(num):
    return int(num, 2)

def main():
    data = []
    for line in read_input('input.txt'):
        data.append(line)
    gamma, epsilon = compute_gamma_epsilon(data)
    result = bin2dec(gamma) * bin2dec(epsilon)
    print(result)

if __name__ == '__main__':
    main()
