def main():
    with open('inputs/inputs1.txt') as f:
        numbers = [line.strip() for line in f]
    print(f'Part 1: {part1(numbers)}')
    print(f'Part 2: {part2(numbers)}') 

def part1(numbers):
    totals = []
    # sum up numbers separated by a newline
    ctr = 0
    for num in numbers:
        if num == '':
            totals.append(ctr)
            ctr = 0
        else:
            ctr += int(num)
        
    return max(totals)

def part2(numbers):
    totals = []
    # sum up numbers separated by a newline
    ctr = 0
    for num in numbers:
        if num == '':
            totals.append(ctr)
            ctr = 0
        else:
            ctr += int(num)
        
    return sum(sorted(totals)[-3:])

if __name__ == '__main__':
    main()