def read_file(filepath):
    groups, group = [], []
    with open(filepath) as fd:
        lines = fd.readlines()
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                groups.append(group)
                group = []
            else:
                group.append(line)
        else:
            groups.append(group)
    return groups

def main():
    result = 0
    groups = read_file("input.txt")
    for group in groups:
        person = group[0]
        rest_group = group[1:]
        for ans in person:
            for rest_person in rest_group:
                if ans in rest_person




if __name__ == '__main__':
    main()