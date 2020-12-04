with open("input.txt") as f:
    data = f.read().split("\n\n")

valid = 0

for line in data:
    if line.count(':') == 8 or (line.count(":") == 7 and not line.count("cid:")):
        valid += 1

print(valid)
