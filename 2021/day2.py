# read numbers from inputs.txt and count the number of times they increase
def main():
    with open('inputs/inputs2.txt') as f:
        data = f.readlines()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}') 

# thanks copilot for making a (wrong) part 2 function even tho I haven't read it
def part1(commands):
    depth = hpos = aim = 0
    for command in commands:
        cmd, val = command.split(" ")
        if cmd == 'down':
            depth += int(val)
        elif cmd == 'up':
            depth -= int(val)
        elif cmd == 'forward':
            hpos += int(val)
    return hpos * depth

# for part2, determine when 3 member sliding window is increasing
def part2(commands):
    depth = hpos = aim = 0
    for command in commands:
        cmd, val = command.split(" ")
        if cmd == 'down':
            aim += int(val)
        elif cmd == 'up':
            aim -= int(val)
        elif cmd == 'forward':
            hpos += int(val)
            depth += int(val) * aim
    return hpos * depth

if __name__ == '__main__':
    main()
