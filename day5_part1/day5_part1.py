def read_file(f_in):
    with open(f_in, 'r') as f:
        return list(line.split() for line in f.readlines())


def main():
    file = read_file('day5_input')
    print(file[0:4])


if __name__ == "__main__":
    main()  # Prints ..
    