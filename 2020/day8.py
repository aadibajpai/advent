with open("input.txt") as f:
    lines = f.read().splitlines()


def f(lines):
    acc = 0
    visited = set()

    i = 0
    while i < len(lines):
        if i in visited:
            return None
        line = lines[i]
        visited.add(i)
        if line[:3] == "acc":
            acc += int(line[4:])
        elif line[:3] == "jmp":
            i += int(line[4:])
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
