# read numbers from inputs.txt and count the number of times they increase
def main():
    with open('inputs/inputs5.txt') as f:
        # read file without newline characters
        data = f.read().splitlines()
        # every line is of form x1,y1 -> x2,y2 read it into numbers
        numbers = []
        for line in data:
            numbers.append(list(map(lambda x: tuple(map(int, x.split(','))), line.split(' -> '))))
    print(f'Part 1: {part1(numbers)}')
    # print(f'Part 2: {part2(tables, numbers)}') 


def part1(lines):
    board = bounds(lines)
    for line in lines:
        x, y = line
        x1, y1 = x
        x2, y2 = y
        board[y2][x2] += 1
        while x1 != x2 or y1 != y2:
            board[y1][x1] += 1
            x1 += 1 if x2 > x1 else 0 if x1 == x2 else -1
            y1 += 1 if y2 > y1 else 0 if y1 == y2 else -1  
    c = sum([1 for x in board for y in x if y > 1])
    return c

    
# find the bounds of the 2d array of lines given coordinates
def bounds(lines):
    xmax = max([max(x[0][0], x[1][0]) for x in lines])
    ymax = max([max(x[0][1], x[1][1]) for x in lines])
    # make 2d array of zeros with bounds
    board = [[0 for x in range(xmax+1)] for y in range(ymax+1)]
    # print(xmax, ymax)
    return board
    
# def hlep(line):
#     x, y = line
#     x1, y1 = x
#     x2, y2 = y
#     if x1 == x2:
#         return "v"
#     elif y1 == y2:
#         return "h"
#     else:
#         return "d"


def part2(boards, numbers):
    pass

if __name__ == '__main__':
    main()
