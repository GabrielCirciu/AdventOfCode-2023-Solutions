def read_file(f_name):
    with open(f_name, 'r') as f:
        return [line.split() for line in f.readlines()]

def process_line(f):
    for line in f:
        for i in range(len(line)):
            line[i] = line[i].strip(',;:')
    return f

def valid_number(lin, num_che) -> int:
    for i in range(2, len(lin)-1, 2):
        if int(lin[i]) > num_che[lin[i+1]]:
            return 0
    return int(lin[1])

def main():
    file = process_line(read_file('day2_input'))
    num_check = { 'red': 12, 'green': 13, 'blue': 14 }
    valid_sum = 0
    for line in file:
        valid_sum += valid_number(line, num_check)
    print(valid_sum)

if __name__ == "__main__":
    main()
