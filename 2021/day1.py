# read numbers from inputs.txt and count the number of times they increase
def main():
    with open('inputs.txt') as f:
        numbers = [int(line.strip()) for line in f]
    print(f'Part 1: {part1(numbers)}')
    print(f'Part 2: {part2(numbers)}') 

# thanks copilot for making a (wrong) part 2 function even tho I haven't read it
def part1(numbers):
    count = 0
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i+1]:
            count += 1
    return count

# for part2, determine when 3 member sliding window is increasing
def part2(numbers):
    count = 0
    for i in range(len(numbers) - 3):
        if numbers[i] + numbers[i+1] + numbers[i+2 ] < numbers[i+1] + numbers[i+2] + numbers[i+3]:
            count += 1
    return count

if __name__ == '__main__':
    main()