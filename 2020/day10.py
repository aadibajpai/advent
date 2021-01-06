#!/usr/bin/env python3
from functools import cache

with open("input.txt") as f:
    lines = f.read().splitlines()

lines = sorted([int(line) for line in lines])
lines = [0] + lines + [max(lines)+3]
three = one = 0


for x, y in zip(lines, lines[1:]):
    if y - x == 1:
        one += 1
    elif y - x == 3:
        three += 1

print(one*three)


@cache
def soln(i):
    if i == len(lines) - 1:
        return 1
    count = 0
    for x in range(i+1, min(i+4, len(lines))):  # avoid out of bounds
        if lines[x] - lines[i] <= 3:
            count += soln(x)
    return count


print(soln(0))
