# read numbers from inputs.txt and count the number of times they increase
def main():
    with open('inputs/inputs11.txt') as f:
        # read file without newline characters
        data = [[int(i) for i in line.split()] for line in f.read().splitlines()]
        # for line in f.readlines():
        #     data.append([int(i) for i in line.strip()])

    print(f'Part 1: {part1(data[:])}')
    print(f'Part 2: {part2(data[:])}') 


def match(chr, stack):
    if chr in starts:
        stack.append(chr)
    elif chr in ends:
        if stack.pop() != mat[chr]:
            return points[chr]
    return 0

def part1(lines):
    

def part2(lines):
    pass

if __name__ == '__main__':
    main()
