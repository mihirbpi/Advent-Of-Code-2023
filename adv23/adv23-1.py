from aocd import get_data
import re
import sys
sys. setrecursionlimit(1000000)

data = get_data(year=2023, day=23)
grid_dict = {}

for i in range(len(data.split("\n"))):

    for j in range(len(data.split("\n")[0])):
        grid_dict[(i,j)] = data.split("\n")[i][j]

def get_dirs(pos):
    dirs = [(0,-1), (0,1), (-1,0), (1,0)]

    if (grid_dict[pos] in "<>^v"):
        return [dirs["<>^v".index(grid_dict[pos])]]
    return dirs

def dfs(pos, end, visited, depth):

    if (pos == end):
         return (depth, pos)

    res_depth = -1
    res_start = pos

    visited.add(pos)

    for dir in get_dirs(pos):
        neighbor = (pos[0]+dir[0], pos[1]+dir[1])

        if (neighbor in grid_dict and neighbor not in visited and grid_dict[neighbor] in "<>^v." and neighbor not in visited):
            n_res =  dfs(neighbor, end, visited, depth+1)

            if (n_res[0] >= res_depth and n_res[1] == end):
                res_depth, res_start = n_res

    visited.remove(pos)

    if ((res_depth, res_start) == (-1, start)):
        return (depth, start)
        
    return (res_depth, res_start)

start = (0,1)
end = (len(data.split("\n"))-1, len(data.split("\n")[0])-2)
visited = set(start)
print(dfs(start, end, visited, 0)[0])


