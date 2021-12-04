from copy import deepcopy as dc

# read numbers from inputs.txt and count the number of times they increase
def main():
    with open('inputs/inputs4.txt') as f:
        # read file without newline characters
        data = f.read().splitlines()
        numbers = list(map(int, data[0].strip().split(',')))
        data = [line for line in data[2:] if line != ''] 
        tables = []
        # read 5 entries from data and append a list of them to tables
        for i in range(0, len(data), 5):
            board = []
            for j in range(5):
                board.append(list(map(int, data[i+j].strip().split())))
            tables.append(board)
    print(f'Part 1: {part1(dc(tables), numbers)}')
    print(f'Part 2: {part2(tables, numbers)}') 


def part1(boards, numbers):
    for n in numbers:
        for board in boards:
            for i in range(5):
                for j in range(5):
                    if board[i][j] == n:
                        board[i][j] = -1
            if solved(board):
                return score(dc(board))*n
        
    
def score(board):
    for i in range(5):
        for j in range(5):
            if board[i][j] == -1:
                board[i][j] = 0
    s = 0
    for row in board:
        s += sum(row)
    return s



def solved(board):
    for row in board:
        if row.count(-1) == 5:
            return True
    # check if columns are all -1s
    for i in range(5):
        # thanks copilot
        if board[0][i] == -1 and board[1][i] == -1 and board[2][i] == -1 and board[3][i] == -1 and board[4][i] == -1:
            return True
    return False
    


def part2(boards, numbers):
    for n in numbers:
        i = 0
        while i < len(boards):
            for j in range(5):
                for k in range(5):
                    if boards[i][j][k] == n:
                        boards[i][j][k] = -1
            if solved(boards[i]):
                if len(boards) == 1:
                    return score(dc(boards[i]))*n
                # pain can't use remove
                boards.pop(i)
            else:
                i += 1

if __name__ == '__main__':
    main()
