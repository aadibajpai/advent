with open("input.txt") as f:
    grid = [line.strip("\n") for line in f.readlines()]  # readlines was fucking up bc \n

rows = len(grid)  # maybe they should be opposite
cols = len(grid[0])

r = c = trees = 0

while r < rows:
    c += 3
    r += 1

    if r >= rows:
        break

    if grid[r][c % cols] == "#":
        trees += 1

print(trees, r, c, rows, cols)
