with open("input.txt") as f:
    lines = f.read().splitlines()

# id is nothing but the whole binary bc 8 is 2³
seats = [int(line.replace("F", "0").replace("L", "0").replace("B", "1").replace("R", "1"), 2) for line in lines]

print(max(seats))
