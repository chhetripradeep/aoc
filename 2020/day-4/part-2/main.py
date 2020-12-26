import re

def read_input(filepath):
    passports = []
    with open(filepath) as fd:
        lines = fd.readlines()
        passport = {}
        for line in lines:
            if len(line.strip()) == 0:
                passports.append(passport)
                passport = {}
            else:
                fields = line.split()
                for field in fields:
                    k = field.split(":")[0]
                    v = field.split(":")[1]
                    passport[k] = v
    return passports

def is_valid_byr(passport):
    try:
        byr = int(passport['byr'])
    except:
        return False
    if 1920 <= byr <= 2002:
        return True
    return False

def is_valid_iyr(passport):
    try:
        iyr = int(passport['iyr'])
    except:
        return False
    if 2010 <= iyr <= 2020:
        return True
    return False

def is_valid_eyr(passport):
    try:
        eyr = int(passport['eyr'])
    except:
        return False
    if 2020 <= eyr <= 2030:
        return True
    return False

def is_valid_hgt_unit(hgt):
    unit = hgt[-2:]
    if unit == 'in' or unit == 'cm':
        return True
    return False

def is_valid_hgt_value(hgt):
    unit = hgt[-2:]
    value = int(hgt[:-2])
    if unit == 'in' and (59 <= value <= 76):
        return True
    elif unit == 'cm' and (150 <= value <= 193):
        return True
    else:
        return False

def is_valid_hgt(passport):
    try:
        hgt = passport['hgt']
    except:
        return False
    if is_valid_hgt_unit(hgt) and is_valid_hgt_value(hgt):
        return True
    return False

def is_valid_hcl(passport):
    try:
        hcl = passport['hcl']
    except:
        return False
    if re.match(r'#[0-9a-f]{6}', hcl):
        return True
    return False

def is_valid_ecl(passport):
    try:
        ecl = passport['ecl']
    except:
        return False
    valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl in valid:
        return True
    return False

def is_valid_pid(passport):
    try:
        pid = passport['pid']
    except:
        return False
    if len(pid) == 9:
        return True
    return False

def is_valid_passport(passport):
    if is_valid_pid(passport) and is_valid_ecl(passport) and is_valid_hcl(passport) and is_valid_hgt(passport) and is_valid_eyr(passport) and is_valid_iyr(passport) and is_valid_byr(passport):
        return True
    return False

def main():
    result = 0
    passports = read_input("input.txt")
    for passport in passports:
        if is_valid_passport(passport):
            result += 1
    print(result)

if __name__ == '__main__':
    main()