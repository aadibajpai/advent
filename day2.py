with open("input.txt") as f:
    lines = f.readlines()

valid = 0

for line in lines:
    num, ch, passwd = line.split()
    f, c = num.split("-")
    ch = ch.strip(":")

    if (passwd[int(f)-1] == ch) != (passwd[int(c)-1] == ch):  # xor operation
        valid += 1

print(valid)
