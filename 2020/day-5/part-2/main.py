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

def missing_seat(seats):
    for i in range(0, len(seats)-1):
        if seats[i+1] - seats[i] == 2:
            return seats[i] + 1

def calculate_seatid(seat):
    prefix = seat / 10
    suffix = seat % 10
    return prefix * 8 + suffix

def main():
    seats = []
    input = transform(read_file("input.txt"))
    for i in input:
        prefix, suffix = i[:7], i[7:]
        prefix_d, suffix_d = bin_to_dec(prefix), bin_to_dec(suffix)
        seats.append(int(str(prefix_d)+str(suffix_d)))
    seats = sorted(seats)
    missing = missing_seat(seats)
    print(calculate_seatid(missing))

if __name__ == "__main__":
    main()