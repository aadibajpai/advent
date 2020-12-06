with open("input.txt") as f:
    lines = f.read().split("\n\n")

s = 0
print(lines)
for line in lines:
    s += len(set(line.replace("\n", "")))

print(s)
