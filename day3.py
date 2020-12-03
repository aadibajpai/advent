with open("input.txt") as f:
    grid = f.read().splitlines()  # readlines was fucking up bc \n

rows = len(grid)  # maybe they should be opposite
cols = len(grid[0])


def slope(a, b):
    r = c = trees = 0
    while r < rows:
        c += a
        r += b

        if r >= rows:
            break

        if grid[r][c % cols] == "#":
            trees += 1
    return trees


print(slope(1, 1)*slope(3, 1)*slope(5, 1)*slope(7, 1)*slope(1, 2))
