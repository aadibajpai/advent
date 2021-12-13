def main():
    with open('inputs/inputs13.txt') as f:
        data = f.readlines()

    print(f'Part 1: {part1(data[:])}')
    print(f'Part 2: {part2(data[:])}') 


def fold_x(lst, n):
    new_lst = [[lst[j][i] for i in range(n)] for j in range(len(lst))]
    for j in range(len(new_lst)):
        for i in range(len(new_lst[0])):
            new_lst[j][i] = new_lst[j][i] or lst[j][len(lst[0])-1-i]
    return new_lst


def fold_y(lst, n):
    new_lst = [[lst[j][i] for i in range(len(lst[0]))] for j in range(n)]
    for j in range(len(new_lst)):
        for i in range(len(new_lst[0])):
            new_lst[j][i] = new_lst[j][i] or lst[len(lst)-1-j][i]
    return new_lst


def part1(lines):
    pts = []
    folds = []
    for line in lines:
        if not line.strip():
            continue
        if not line.startswith('fold'):
            pts.append(tuple(map(int, line.split(','))))
        else:
            f, n = line.split('=')
            folds.append((f[-1], int(n)))

    # get bounds of list from pts
    x_max = max(pts, key=lambda x: x[0])[0]
    y_max = max(pts, key=lambda x: x[1])[1]
    lst = [[False for _ in range(x_max+1)] for _ in range(y_max+1)]
    for x, y in pts:
        lst[y][x] = True
    
    p1 = True

    for f, n in folds:
        lst = fold_x(lst, n) if f == 'x' else fold_y(lst, n)
        if p1:
            print("Part 1: ", sum(sum(row) for row in lst))
            p1 = False

    # count number of True values in lst
    # replace True with # and False with space
    lst = [[' ' if not x else '#' for x in row] for row in lst]
    for row in lst:
        print(''.join(row))
    

def part2(lines):
    pass

if __name__ == '__main__':
    main()
