from collections import defaultdict
# read numbers from inputs.txt and count the number of times they increase
def main():
    with open('inputs/inputs7.txt') as f:
        # read file without newline characters
        data = list(map(int, f.readline().split(',')))
        
    print(f'Part 1: {part1(data[:])}')
    print(f'Part 2: {part2(data[:])}') 


def part1(lines):
    # find minimal movements to align all numbers
    # arbitrary random big number
    min_move = 1000000000
    for i in range(len(lines)):
        diff = 0
        for j in range(len(lines)):
            diff += abs(lines[j] - lines[i])
        if diff < min_move:
            # update the minimal difference
            min_move = diff
    return min_move


def part2(lines):
    # find minimal movements to align all numbers
    min_move = 1000000000
    for i in range(len(lines)):
        diff = 0
        for j in range(len(lines)):
            # sigma n = n * (n + 1) / 2
            diff += abs(lines[j] - lines[i]) * (abs(lines[j] - lines[i]) + 1) // 2
        min_move = min(min_move, diff)
    return min_move

if __name__ == '__main__':
    main()
