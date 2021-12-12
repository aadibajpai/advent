# read numbers from inputs.txt and count the number of times they increase
from copy import deepcopy as dc
def main():
    with open('inputs/inputs11.txt') as f:
        # read file without newline characters
        data = [[int(i) for i in line] for line in f.read().splitlines()]
        # for line in f.readlines():
        #     data.append([int(i) for i in line.strip()])
    # print(data)
    print(f'Part 1: {part1(dc(data))}')
    print(f'Part 2: {part2(dc(data))}') 


def neighbors(i, j, lines, flashed):
    n = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x == i and y == j:
                continue
            if 0 <= x < 10 and 0 <= y < 10:
                lines[x][y] += 1
                if lines[x][y] > 9 and not flashed[x][y]:
                    n += flash(x, y, lines, flashed)
    return n


def flash(i, j, lines, flashed):
    flashes = 0
    lines[i][j] += 1

    if lines[i][j] > 9 and not flashed[i][j]:
        flashes += 1
        flashed[i][j] = True
        # check neighbours
        flashes += neighbors(i, j, lines, flashed)
        
    return flashes

def step(lines, flashed):
    flashes = 0
    for i in range(10):
        for j in range(10):
            flashes += flash(i, j, lines, flashed)
    return flashes

def part1(lines):
    flashes = 0
    
    for _ in range(100):
        flashed = [[False]*10 for _ in range(10)]
        flashes += step(lines, flashed)

        for i in range(10):
            for j in range(10):
                if flashed[i][j]:
                    lines[i][j] = 0

    return flashes


def part2(lines):
    steps = 0
    
    while True:
        flashed = [[False]*10 for _ in range(10)]
        step(lines, flashed)
        steps += 1

        for i in range(10):
            for j in range(10):
                if flashed[i][j]:
                    lines[i][j] = 0
        # check lines all 0s
        if all(all(line == 0 for line in line_) for line_ in lines):
            return steps


if __name__ == '__main__':
    main()
