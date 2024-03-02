import os

with open('problem_input', 'r') as file:
    lines = file.readlines()

lines = [list(line.strip()) for line in lines]
total = 0

for line in lines:
    digits = ['0','0']
    for i in range(len(line)):
        if line[i].isdigit():
            digits[0] = line[i]
            break
    for i in range(len(line)):
        if line[i].isdigit():
            digits[1] = line[i]
    number = int(digits[0] + digits[1])
    total += number

print(total)
