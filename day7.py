with open("input.txt") as f:
    lines = f.read().splitlines()

s = set()
bags = {''.join(line.split()[:2]): [] for line in lines}

for line in lines:
    if "no other" in line:
        continue
    line = line.split()
    bag = line[0] + line[1]
    for i in range(3, len(line)):
        if line[i].startswith("bag"):
            bags[bag].append(line[i-2]+line[i-1])

hold = [""]
x = "shinygold"
while x:
    for k, v in bags.items():
        if x in v:
            s.add(k)
            hold.append(k)
    x = hold.pop()

print(len(s))
