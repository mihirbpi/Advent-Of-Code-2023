from aocd import get_data
import re
import sys
sys. setrecursionlimit(1000000)

data = get_data(year=2023, day=23)
grid_dict = {}

for i in range(len(data.split("\n"))):

    for j in range(len(data.split("\n")[0])):
        grid_dict[(i,j)] = data.split("\n")[i][j]
    
start = (0,1)
end = (len(data.split("\n"))-1, len(data.split("\n")[0])-2)

positions = set([start, end])

for pos in grid_dict: 
    n_neighbors = 0

    if (pos in grid_dict and grid_dict[pos] in "<>^v."):

        for dir in [(0,-1), (0,1), (-1,0), (1,0)]:
             neighbor = (pos[0]+dir[0], pos[1]+dir[1])

             if (neighbor in grid_dict and grid_dict[neighbor] in "<>^v."):
                 n_neighbors += 1

        if (n_neighbors >= 3):
            positions.add(pos)

graph = {pos: {} for pos in positions}

for pos in positions:
    stack = [(pos,0)]
    visited = set([pos])

    while(len(stack) > 0):
        next_pos, steps = stack.pop()

        if (next_pos != pos and next_pos in positions):
            graph[pos][next_pos] = steps
            continue

        for dir in [(0,-1), (0,1), (-1,0), (1,0)]:
            neighbor = (next_pos[0]+dir[0], next_pos[1]+dir[1])

            if (neighbor in grid_dict and grid_dict[neighbor] in "<>^v." and neighbor not in visited):
                    visited.add(neighbor)
                    stack.append((neighbor, steps+1))

visited = set()

def dfs(pos, end, visited, depth):

    if (pos == end):
        return depth

    res = -1
    visited.add(pos)

    for neighbor in graph[pos]:

        if (neighbor not in visited):
            res = max(res, dfs(neighbor, end, visited, depth + graph[pos][neighbor]))

    visited.remove(pos)
    return res

print(dfs(start, end, visited, 0))


