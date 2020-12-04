import re

with open("input.txt") as f:
    data = f.read().split("\n\n")

valid = 0

byr = re.compile(r"byr:(\d{4})")
iyr = re.compile(r"iyr:(\d{4})")
eyr = re.compile(r"eyr:(\d{4})")

hi = re.compile(r"hgt:(\d{2})in")
hc = re.compile(r"hgt:(\d{3})cm")

hcl = re.compile(r"hcl:#([0-9a-f]{6})")
ecl = re.compile(r"ecl:([a-z]{3})")

pid = re.compile(r"pid:(\d*)")  # assert exact 9 later


for line in data:
    line = line.replace("\n", " ")
    if line.count(":") == 8 or (line.count(":") == 7 and not line.count("cid:")):
        try:
            m = int(re.search(byr, line).group(1))

            if m < 1920 or m > 2002:
                continue

            i = int(re.search(iyr, line).group(1))

            if 2010 > i or i > 2020:
                continue

            e = int(re.search(eyr, line).group(1))

            if e < 2020 or e > 2030:
                continue

            h = int((re.search(hi, line) or re.search(hc, line)).group(1))

            if len(str(h)) == 2 and (h < 59 or h > 76):
                continue

            if len(str(h)) == 3 and (h < 150 or h > 193):
                continue

            hh = re.search(hcl, line).group(1)

            if not hh:
                continue

            ee = re.search(ecl, line).group(1)

            if ee not in ["amb", "blu", "brn", "grn", "gry", "hzl", "oth"]:
                continue

            pp = re.search(pid, line).group(1)

            if not (len(pp) == 9):
                continue

            print(line)
            valid += 1
        except Exception:
            continue


print(valid)
