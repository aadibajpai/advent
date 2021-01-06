#!/usr/bin/env python3
with open("input.txt") as f:
    lines = f.read().splitlines()

r = len(lines)
c = len(lines[0])
changed = True

def adj(i, j, L):
    empty = 0
    seats = 0
    arr = [(0+1, 0),(0, 0+1),(0-1, 0),(0, 0-1),(0+1, 0+1),
            (0-1, 0-1),(0+1, 0-1),(0-1, 0+1)]
    for x in arr:
        a, b = x
        if not (0 <= i+a < r and 0 <= j+b < c):
            continue
        ch = lines[i+a][j+b]
        t = 1
        while 0 <= i+a*t < r and 0 <= j+b*t < c:
            if ch != ".":
                break
            else:
                ch = lines[i+a*t][j+b*t]
                t += 1

        if ch == "L":
            empty += 1
            seats += 1
        elif ch == "#":
            seats += 1
    if L:
        return seats - empty == 0
    return seats - empty >= 5

while True:
    owo = []
    for i in range(r):
        row = ""
        for j in range(c):
            if lines[i][j] == "L" and adj(i, j, True):
                row += "#"
            elif lines[i][j] == "#" and adj(i, j, False):
                row += "L"
            else:
                row += lines[i][j]
        owo.append(row)
    if owo == lines:
          break

    lines = owo[:]

c = 0
for x in owo:
    c += x.count("#")

print(c)
