def main():
    with open('inputs/inputs2.txt') as f:
        oppn_move =[]
        our_move = []
        for line in f:
            oppn, our = line.strip().split(' ')
            oppn_move.append(oppn)
            # our_move.append(our)
            # part 2
            if oppn == "A":
                if our == "X":
                    our_move.append("Z")
                elif our == "Y":
                    our_move.append("X")
                else:
                    our_move.append("Y")
            elif oppn == "B":
                if our == "X":
                    our_move.append("X")
                elif our == "Y":
                    our_move.append("Y")
                else:
                    our_move.append("Z")
            else:
                if our == "X":
                    our_move.append("Y")
                elif our == "Y":
                    our_move.append("Z")
                else:
                    our_move.append("X")


    # print(f'Part 1: {part1(oppn_move, our_move)}')
    print(f'Part 2: {part1(oppn_move, our_move)}') 

def part1(their, ours):
    score = 0
    for oppn, our in zip(their, ours):
        if our == "X":
            score += 1
        elif our == "Y":
            score += 2
        else:
            score += 3

        if (oppn == "A" and our == "X") or (oppn == "B" and our == "Y") or (oppn == "C" and our == "Z"):
            score += 3
        elif (oppn == 'A' and our == 'Y') or (oppn == 'B' and our == 'Z') or (oppn == 'C' and our == 'X'):
            score += 6
        elif (oppn == 'A' and our == 'Z') or (oppn == 'B' and our == 'X') or (oppn == 'C' and our == 'Y'):
            score += 0

    return score

def part2(numbers):
    totals = []
    # sum up numbers separated by a newline
    ctr = 0
    for num in numbers:
        if num == '':
            totals.append(ctr)
            ctr = 0
        else:
            ctr += int(num)
        
    return sum(sorted(totals)[-3:])

if __name__ == '__main__':
    main()