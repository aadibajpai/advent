# read numbers from inputs.txt and count the number of times they increase
def main():
    with open('inputs/inputs3.txt') as f:
        # read file every line is a number
        data = f.read().splitlines()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}') 

# thanks copilot for making a (wrong) part 2 function even tho I haven't read it
def part1(data):
    total = len(data)
    i = 0
    gamma = ""
    epsilon = ""
    for i in range(len(data[0])):
        zeros = 0
        for number in data:
            if number[i] == '0':
                zeros += 1
        if zeros > total/2:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return int(gamma, 2) * int(epsilon, 2)


def hlep(arr, flag):
    arr = arr[:]
    numb = "0" if flag == 0 else "1"
    other_num = "1" if flag == 0 else "0"
    for i in range(len(arr[0])):
        total = len(arr)
        zeros = 0
        for number in arr:
            if number[i] == '0':
                zeros += 1
        if zeros > total/2:
            arr = [num for num in arr if num[i] == numb]
        elif zeros == total/2:
            arr = [num for num in arr if num[i] == other_num]
        else:
            arr = [num for num in arr if num[i] == other_num]
        if len(arr) == 1:
            return arr[0]


def part2(data):
    ox = hlep(data[:], 0)
    co2 = hlep(data[:], 1)
    return int(ox, 2) * int(co2, 2)

if __name__ == '__main__':
    main()
