# read numbers from inputs.txt and count the number of times they increase
def main():
    with open('inputs/inputs9.txt') as f:
        # read file without newline characters
        data = []
        for line in f.readlines():
            data.append([int(i) for i in line.strip()])

    print(f'Part 1: {part1(data[:])}')
    print(f'Part 2: {part2(data[:])}') 

def find(i, j, lines):
    # find surrounding points that are not 9
    if lines[i][j] == 9:
        return 0
    lines[i][j] = 9
    pts = 1
    for k in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if k[0] < 0 or k[1] < 0 or k[0] >= len(lines) or k[1] >= len(lines[i]):
            continue
        pts += find(k[0], k[1], lines)

    return pts

def part1(lines):
    ctr = []
    risk = 0
    ans = 1

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            # check number is lower than neighbours
            valid = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for k in valid:
                if k[0] < 0 or k[1] < 0 or k[0] >= len(lines) or k[1] >= len(lines[i]):
                    continue
                if lines[i][j] >= lines[k[0]][k[1]]:
                    break
            else:
                risk += 1 + lines[i][j]
                ctr.append(find(i, j, lines))

    for i in sorted(ctr)[-3:]:
        ans *= i    
    print("part 2: ", ans) 
    return risk

def part2(lines):
    pass

if __name__ == '__main__':
    main()
