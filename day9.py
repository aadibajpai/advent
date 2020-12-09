#!/usr/bin/env python3
with open("input.txt") as f:
    lines = f.read().splitlines()

lines = [int(li) for li in lines]
pre = [lines[i] for i in range(25)]

linez = lines[25:]

for line in linez:
    for i in pre:
        if line - i in pre:
            pre.pop(0)
            pre.append(line)
            break
    else:
        print(line)
        ll = line
        break

# actually use a sliding window
# for i in range(len(lines)):
#     for j in range(i+2, len(lines)):
#         window = lines[i:j]
#         if sum(window) == ll:
#             print(min(window) + max(window))

# optimized and much more cooler

start = end = ss = 0
while ss != ll:
    if ss < ll:
        ss += lines[end]
        end += 1
    else:
        ss -= lines[start]
        start += 1

arr = lines[start:end]
print(min(arr) + max(arr))
