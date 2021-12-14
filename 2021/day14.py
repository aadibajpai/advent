from copy import deepcopy as dc
from collections import Counter

def main():
    with open('inputs/inputs14.txt') as f:
        ss = f.readline().strip()
        # print(ss)
        rules = {}
        f.readline()
        for line in f.readlines():
            pair, mid = line.strip().split(' -> ')
            rules[pair] = mid

    print(f'Part 1: {part1(ss, dc(rules))}')
    print(f'Part 2: {part2(rules)}') 


def part1(string, rules):
    # iterate through consecutive characters in ss
    ss = Counter()
    for i, j in zip(string, string[1:]):
        ss[i+j] += 1

    for _ in range(40):
        cc = Counter()
        for i in ss:
            cc[i[0]+rules[i]] += ss[i]
            cc[rules[i]+i[1]] += ss[i]
        ss = cc
        if _ in [9, 39]:
            c = Counter()
            for i in ss:
                c[i[0]] += ss[i]
            # print most common count - least common count
            # off by one pain
            print(c.most_common()[0][1] - c.most_common()[-1][1] + 1)
    

def part2(lines):
    pass

if __name__ == '__main__':
    main()
