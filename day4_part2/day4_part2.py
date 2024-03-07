def read_file(f_in):
    with open(f_in, 'r') as f:
        return [list(line.split("|")) for line in f.readlines()]


def reformat(f_in):
    for line in f_in:
        line[0] = list(map(int, line[0][10:-1].split()))
        line[1] = list(map(int, line[1][1:-1].split()))
    return f_in


def process_file(l_in):
    counters = [1] * (len(l_in)+20)
    for i in range(len(l_in)):
        extender = 0
        for element in l_in[i][0]:
            if element in l_in[i][1]:
                extender += 1
        if extender > 0:
            for j in range(i+1, i+extender+1):
                counters[j] += counters[i]
    return sum(counters[0:len(l_in)])


def main():
    file = reformat(read_file('day4_input'))
    print(process_file(file))


if __name__ == "__main__":
    main()  # Prints 5422730, which is the correct answer
