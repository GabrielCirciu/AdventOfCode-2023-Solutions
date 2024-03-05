import re

def read_file(file_name):
    with open(file_name, 'r') as file:
        return [line for line in file.readlines()]

def find_digits(line, digits_table):
    indexes = []
    for (digit, value) in digits_table.items():
        if line.find(digit) != -1:
            for m in re.finditer(digit, line):
                indexes.append((m.start(), value))
    indexes.sort()
    return indexes[0][1], indexes[-1][1]

def main():
    digits_table = { 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, '0': 0, '1': 1, '2': 2, '3': 3,
        '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 }
    total = 0
    for line in read_file('problem_input'):
        first, last = find_digits(line, digits_table)
        total += int(f"{first}{last}")
    print(total)

if __name__ == '__main__':
    main()  # Prints 54706 which is the correct answer
