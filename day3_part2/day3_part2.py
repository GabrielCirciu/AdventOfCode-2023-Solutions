def read_file(f_in):
    with open(f_in, 'r') as f:
        return [list(line[:-1]) for line in f.readlines()]

def expand_edges(file):
    dots = ['.'] * len(file[0])
    file = [dots] + file + [dots]
    for i in range(len(file)):
        file[i] = ['.'] + file[i] + ['.']
    return file

def find_numbers(file):
    star_dict = {}
    sum_counter = 0
    row = 0
    while row < len(file):
        col = 0
        start_xy, end_xy = [0, 0], [0, 0]
        while col < len(file[row]):
            if file[row][col].isdigit():
                start_xy = [row-1, col-1]
                end_index = col
                while file[row][end_index].isdigit():
                    end_index += 1
                end_xy = [row+1, end_index]
                number = int(''.join(file[row][col:end_index]))
                star_dict = search_around(file, start_xy, end_xy, number, star_dict)
                col = end_index
            col += 1
        row += 1
    for key in star_dict:
        if star_dict[key][0] == 2:
            sum_counter += star_dict[key][1]
    return sum_counter

def search_around(file, start_i, end_i, num, s_dict):
    for i in range(start_i[0], end_i[0]+1):
        for j in range(start_i[1], end_i[1]+1):
            if file[i][j] == '*':
                if (i, j) in s_dict:
                    s_dict[(i, j)][0] += 1
                    s_dict[(i, j)][1] = s_dict[(i, j)][1] * num
                else:
                    s_dict[(i, j)] = [1, num]
    return s_dict

def main():
    file = expand_edges(read_file('day3_input'))
    print(find_numbers(file))

if __name__ == "__main__":
    main()  # Prints 84399773, which is the correct answer
