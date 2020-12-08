with open("input.txt") as f:
    lines = f.read().splitlines()

acc = 0
visited = [False for _ in range(len(lines))]

i = 0
while i < len(lines):
    if visited[i]:
        break
    l = lines[i]
    visited[i] = True
    if l[:3] == "acc":
        acc += int(l[4:])
    elif l[:3] == "jmp":
        i += int(l[4:])
        continue
    i += 1

print(acc)
