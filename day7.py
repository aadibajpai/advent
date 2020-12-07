with open("input.txt") as f:
    lines = f.read().splitlines()

s = 1
bags = {''.join(line.split()[:2]): [] for line in lines}

for line in lines:
    if "no other" in line:
        continue
    line = line.split()
    bag = line[0] + line[1]
    for i in range(3, len(line)):
        if line[i].startswith("bag"):
            bags[bag].append((int(line[i-3]), line[i-2]+line[i-1]))


x = "shinygold"
print(bags)


def f(x):
    s = 1
    if (vals := bags[x]):
        print(vals)
        for i in vals:
            n, k = i
            print(n, k)
            s += n * f(k)
    return s


s = f(x) - 1  # subtract 1 since we don't want to count shiny gold itself

print(s)
