
def read_file(filepath):
    input = []
    with open(filepath) as fd:
        lines = fd.readlines()
        for line in lines:
            input.append(line.strip())
    return input

def transform(input):
    output = []
    for i in input:
        i = i.replace('F', '0')
        i = i.replace('B', '1')
        i = i.replace('L', '0')
        i = i.replace('R', '1')
        output.append(i)
    return output

def bin_to_dec(n):
    return int(n, 2)

def main():
    result = []
    input = transform(read_file("input.txt"))
    for i in input:
        prefix, suffix = i[:7], i[7:]
        prefix_d, suffix_d = bin_to_dec(prefix), bin_to_dec(suffix)
        result.append(prefix_d * 8 + suffix_d)
    print(max(result))

if __name__ == "__main__":
    main()