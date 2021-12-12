# read numbers from inputs.txt and count the number of times they increase
def main():
    with open('inputs/inputs10.txt') as f:
        # read file without newline characters
        data = f.readlines()
        # for line in f.readlines():
        #     data.append([int(i) for i in line.strip()])

    print(f'Part 1: {part1(data[:])}')
    print(f'Part 2: {part2(data[:])}') 

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
points2 = {'(': 1, '[': 2, '{': 3, '<': 4}
starts = ['(', '[', '{', '<']
ends = [')', ']', '}', '>']
# map end to starts
mat = {')': '(', ']': '[', '}': '{', '>': '<'}

def match(chr, stack):
    if chr in starts:
        stack.append(chr)
    elif chr in ends:
        if stack.pop() != mat[chr]:
            return points[chr]
    return 0


def part1(lines):
    # match braces per line and output failure if not matching
    score = 0
    scores2 = []

    for line in lines:
        s2 = 0
        stack = []
        f = False
        
        for c in line:
            p = match(c, stack)
            if p:
                score += p
                f = True
                break
        if f:
            continue

        for c in reversed(stack):
            s2 *= 5
            s2 += points2[c]
        scores2.append(s2)
    # return middle scores2 value
    return score, sorted(scores2)[len(scores2)//2]

def part2(lines):
    pass

if __name__ == '__main__':
    main()
