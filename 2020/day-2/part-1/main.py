#!/usr/bin/env python3

import sys

def read_input(filename):
    policies = []
    passwords = []
    with open(filename) as fd:
        lines = fd.readlines()
        for line in lines:
            line = line.split(':')
            policies.append(line[0].strip())
            passwords.append(line[1].strip())
    return policies, passwords

def is_valid(policy, password):
    policy = policy.split()
    count, character = policy[0].split('-'), policy[1]
    minimum, maximum = int(count[0]), int(count[1])
    num = 0
    for i in password:
        if i == character:
            num += 1
    if num >= minimum and num <= maximum:
        return True
    return False

def calculate(policies, passwords):
    valid_passwords = 0
    for i in range(0, len(policies)):
        if is_valid(policies[i], passwords[i]):
            valid_passwords += 1
    return valid_passwords

def main():
    policies, passwords = read_input("input.txt")
    result = calculate(policies, passwords)
    print(result)

if __name__ == '__main__':
    sys.exit(main())