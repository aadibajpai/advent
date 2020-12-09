#!/usr/bin/env python3
with open("input.txt") as f:
    lines = f.read().splitlines()

pre = [int(lines[i]) for i in range(25)]

lines = lines[25:]

for line in lines:
    for i in pre:
        if int(line) - i in pre:
            pre.pop(0)
            pre.append(int(line))
            break
    else:
        print(line)
        break
