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
    results = []
    groups = read_file("input.txt")
    for group in groups:
        group_ans = ''
        for person in group:
            group_ans += person
        results.append(len(set(group_ans)))
    print(sum(results))

if __name__ == '__main__':
    main()