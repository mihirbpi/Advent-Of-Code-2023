from aocd import get_data
import re
import sys
sys. setrecursionlimit(1000000)

data = get_data(year=2023, day=23)
grid_dict = {}

for i in range(len(data.split("\n"))):
    for j in range(len(data.split("\n")[0])):
        grid_dict[(i,j)] = data.split("\n")[i][j]

def dfs(start, end, visited, depth):

    dirs = [(0,-1), (0,1), (-1,0), (1,0)]
    new_visited = visited.copy()

    if (grid_dict[start] in "<>^v"):
        dir = dirs["<>^v".index(grid_dict[start])]
        neighbor = (start[0] + dir[0], start[1] + dir[1])

        if (neighbor in grid_dict and neighbor not in visited and grid_dict[neighbor] in "<>^v."):
            new_visited.add(neighbor)
            n_res = dfs(neighbor, end, new_visited, depth+1)
            new_visited.remove(neighbor)

            if (n_res[1] == end):
                return n_res
            
            return (depth, start)
        else:
            return (depth, start)
        
    elif (grid_dict[start] == "."):
        res_depth = -1
        res_start = start

        for dir in dirs:
            neighbor = (start[0]+dir[0], start[1]+dir[1])

            if (neighbor in grid_dict and neighbor not in visited and grid_dict[neighbor] in "<>^v."):
                new_visited.add(neighbor)
                n_res =  dfs(neighbor, end, new_visited, depth+1)
                new_visited.remove(neighbor)

                if (n_res[0] >= res_depth and n_res[1] == end):
                    res_depth, res_start = n_res

        if ((res_depth, res_start) == (-1, start)):
            return (depth, start)
        
        return (res_depth, res_start)

start = (0,1)
end = (len(data.split("\n"))-1, len(data.split("\n")[0])-2)
visited = set(start)
print(dfs(start, end, visited, 0)[0])


