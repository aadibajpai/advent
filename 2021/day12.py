from copy import deepcopy as dc
from collections import defaultdict
def main():
    with open('inputs/inputs12.txt') as f:
        # read file without newline characters
        data = f.readlines()
        # for line in f.readlines():
        #     data.append([int(i) for i in line.strip()])

    print(f'Part 1: {part1(dc(data))}')
    print(f'Part 2: {part2(data)}') 

def explore2(graph, pt, visited, dupe=None):
    paths = 0
    if pt == 'end':
        return 1
    if pt == 'start' and visited:
        return 0
    if pt.islower() and pt in visited:
        if not dupe:
            dupe = pt
        else:
            return 0
    # recursively explore till end
    # use | instead of add so it creates a new set
    visited = visited | {pt}
    for i in graph[pt]:  
        paths += explore2(graph, i, visited, dupe)
    return paths

def explore(graph, pt, visited):
    paths = 0
    if pt == 'end':
        return 1

    if pt.islower() and pt in visited:
        return 0
    # recursively explore till end
    # use | instead of add so it creates a new set
    visited = visited | {pt}
    for i in graph[pt]:  
        paths += explore(graph, i, visited)
    return paths

def part1(lines):
    paths = 0
    graph = defaultdict(list)
    for line in lines:
        x, y = line.strip().split('-')
        graph[x].append(y)
        graph[y].append(x)

    paths += explore(graph, "start", set())
    return paths


def part2(lines):
    paths = 0
    graph = defaultdict(list)
    for line in lines:
        x, y = line.strip().split('-')
        graph[x].append(y)
        graph[y].append(x)

    paths += explore2(graph, "start", set(), dupe=None)
    return paths

if __name__ == '__main__':
    main()
