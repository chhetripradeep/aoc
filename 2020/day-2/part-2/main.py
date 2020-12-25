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
    pos1, pos2 = int(count[0]), int(count[1])
    if password[pos1-1] == character and password[pos2-1] != character:
        return True
    elif password[pos1-1] != character and password[pos2-1] == character:
        return True
    else:
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