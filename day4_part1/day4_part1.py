def read_file(f_in):
    with open(f_in, 'r') as f:
        return [list(line.split("|")) for line in f.readlines()]

def reformat(f_in):
    for line in f_in:
        line[0] = list(map(int, line[0][10:-1].split()))
        line[1] = list(map(int, line[1][1:-1].split()))
    return f_in

def process_line(line):
    counter = 0
    for num in line[0]:
        if num in line[1]:
            counter += 1
    if counter > 0:
        return 2 ** (counter - 1)
    return 0

def main():
    file =  reformat(read_file('day4_input'))
    sum_count = 0
    for line in file:
        sum_count += process_line(line)
    print(sum_count)

if __name__ == "__main__":
    main()  # Prints 24733, which is the correct answer
