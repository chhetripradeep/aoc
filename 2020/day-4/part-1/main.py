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

def is_valid_passport(passport):
    mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in mandatory_fields:
        if field not in passport:
            return False
    return True

def main():
    result = 0
    passports = read_input("input.txt")
    for passport in passports:
        if is_valid_passport(passport):
            result += 1
    print(result)

if __name__ == '__main__':
    main()