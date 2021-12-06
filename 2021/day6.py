from collections import defaultdict
# read numbers from inputs.txt and count the number of times they increase
def main():
    with open('inputs/inputs6.txt') as f:
        # read file without newline characters
        data = list(map(int, f.readline().split(',')))
        
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}') 

def simulate(data):
    i = 0
    for i in range(len(data)):
        data[i] -= 1
        if data[i] == -1:
            data[i] = 6
            data.append(8)
    data.sort()


def part1(lines):
    i = 0
    while i < 80:
        simulate(lines)
        i += 1
    return len(lines)


def part2(numbers):
    # use dict to not be exponential
    fishes = defaultdict(int)
    for i in numbers:
        fishes[i] += 1

    for _ in range(256):
        tmp = defaultdict(int)
        for k, v in fishes.items():
            if k == 0:
                tmp[8] += v
                tmp[6] += v
            else:
                tmp[k - 1] += v
        fishes = tmp

    return sum(fishes.values())

if __name__ == '__main__':
    main()
