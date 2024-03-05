def read_file(f_name):
    with open(f_name, 'r') as f:
        return [line.split() for line in f.readlines()]

def process_line(f):
    for line in f:
        for i in range(len(line)):
            line[i] = line[i].strip(',;:')
    return f

def valid_number(lin):
    num_max = { 'red': 0, 'green': 0, 'blue': 0}
    for i in range(2, len(lin)-1, 2):
        if int(lin[i]) > num_max[lin[i+1]]:
            num_max[lin[i+1]] = int(lin[i])
    return num_max['red'] * num_max['green'] * num_max['blue']

def main():
    valid_sum = 0
    for line in process_line(read_file('day2_input')):
        valid_sum += valid_number(line)
    print(valid_sum)

if __name__ == "__main__":
    main()  # Prints 83707, which is the correct answer
