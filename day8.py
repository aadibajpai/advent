with open("input.txt") as f:
    lines = f.read().splitlines()


def f(lines):
    acc = 0
    visited = [False for _ in range(len(lines))]

    i = 0
    while i < len(lines):
        if visited[i]:
            return None
        l = lines[i]
        visited[i] = True
        if l[:3] == "acc":
            acc += int(l[4:])
        elif l[:3] == "jmp":
            i += int(l[4:])
            continue
        i += 1
    return acc


for i in range(len(lines)):
    ll = lines[:]
    if ll[i][:3] == "jmp":
        ll[i] = ll[i].replace("jmp", "nop")
    else:
        ll[i] = ll[i].replace("nop", "jmp")
    acc = f(ll)
    if acc:
        print(acc)
