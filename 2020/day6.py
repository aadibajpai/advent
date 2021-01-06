with open("input.txt") as f:
    lines = f.read().split("\n\n")

s = 0

for line in lines:
    ans = [set(x) for x in line.split()]
    s += len(set.intersection(*ans))

print(s)
