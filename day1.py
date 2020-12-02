with open("input.txt") as f:
    lines = f.readlines()

lines = sorted([int(line) for line in lines])

for i in range(198):  # two pointer
    left = i + 1
    r = 199
    print(i)

    while left < r:
        s = lines[i] + lines[left] + lines[r]
        if s == 2020:
            print(lines[i]*lines[left]*lines[r])
            exit()
        elif s < 2020:
            left += 1
        else:
            r -= 1
