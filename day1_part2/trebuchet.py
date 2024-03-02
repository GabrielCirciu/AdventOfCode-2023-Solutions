import os

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def main():
    digits_table = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
        'seven': 7, 'eight': 8, 'nine': 9, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9 }
    total = 0
    lines = read_file('problem_input')

    for line in lines:
        indexes = []
        for (digit, value) in digits_table.items():
            if line.find(digit) != -1:
                indexes.append((line.index(digit), value))
        indexes.sort()
        total += int(f"{indexes[0][1]}{indexes[-1][1]}")

    print(total)

if __name__ == '__main__':
    main()  # Answer should be 54706 but is returning 54761
