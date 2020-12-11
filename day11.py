#!/usr/bin/env python3
with open("input.txt") as f:
    lines = f.read().splitlines()

r = len(lines)
c = len(lines[0])
changed = True

def adj(i, j, L):
    empty = 0
    seats = 0
    arr = [(i+1, j),(i, j+1),(i-1, j),(i, j-1),(i+1, j+1),
            (i-1, j-1),(i+1, j-1),(i-1, j+1)]
    for x in arr:
        a, b = x
# BRUH PYTHON ALLOWS NEGATIVE VALUES LOL
#        try:
#            ch = lines[a][b]
#        except:
#            continue
        if not (0 <= a < r and 0 <= b < c):
            continue
        ch = lines[a][b]
        if ch == "L":
            empty += 1
            seats += 1
        elif ch == "#":
            seats += 1
    if L:
        return seats - empty == 0
    return seats - empty >= 4

while True:
    owo = []
    for i in range(r):
        row = ""
        for j in range(c):
            if lines[i][j] == ".":
                row += "."
            elif lines[i][j] == "L":
                if adj(i, j, True):
                    row += "#"
                else:
                    row += "L"
            else:
                if adj(i, j, False):
                    row += "L"
                else:
                    row += "#"
        owo.append(row)
    if owo == lines:
          break

    lines = owo[:]

c = 0
for x in owo:
    c += x.count("#")

print(c)
