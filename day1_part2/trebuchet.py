import os

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return [list(line.strip()) for line in lines]

def find_digit(line, direction):
    for char in line[::direction]:
        if char.isdigit():
            return char
    return '0'

def main():
    total = 0
    lines = read_file('problem_input')
    for line in lines:
        total += int(find_digit(line, 1) + find_digit(line, -1))
    print(total)

if __name__ == '__main__':
    main()  # Prints 55447, which is the correct answer
