from aocd import get_data
from collections import defaultdict
from collections import deque
import re

data = get_data(year=2023, day=10)
grid_dict = defaultdict(str)
connections_dict = defaultdict(list)

for i in range(len(data.split("\n"))):

    for j in range(len(data.split("\n")[0])):
        grid_dict[(i,j)] = data.split("\n")[i][j]

start = None
for i in range(len(data.split("\n"))):

    for j in range(len(data.split("\n")[0])):

        if (grid_dict[(i,j)] == "|"):
            connections_dict[(i,j)].append((i+1,j))
            connections_dict[(i,j)].append((i-1,j))
        elif (grid_dict[(i,j)] == "-"):
            connections_dict[(i,j)].append((i,j+1))
            connections_dict[(i,j)].append((i,j-1))
        elif (grid_dict[(i,j)] == "L"):
            connections_dict[(i,j)].append((i,j+1))
            connections_dict[(i,j)].append((i-1,j))
        elif (grid_dict[(i,j)] == "J"):
            connections_dict[(i,j)].append((i,j-1))
            connections_dict[(i,j)].append((i-1,j))
        elif (grid_dict[(i,j)] == "7"):
            connections_dict[(i,j)].append((i,j-1))
            connections_dict[(i,j)].append((i+1,j))
        elif (grid_dict[(i,j)] == "F"):
            connections_dict[(i,j)].append((i,j+1))
            connections_dict[(i,j)].append((i+1,j))

for i in range(len(data.split("\n"))):

    for j in range(len(data.split("\n")[0])):

        if(grid_dict[(i,j)] == "S"):
            start = (i,j)

            for dir in [[1,0], [-1,0], [0,1], [0,-1]]:
                adj_pos = (i+dir[0], j+dir[1])

                if (i,j) in connections_dict[adj_pos] and grid_dict[adj_pos] != "":
                    connections_dict[(i,j)].append(adj_pos)      

queue = deque()
queue.append((start, 0))
visited = set()
dists = {}

while(len(queue) > 0):
    curr, curr_dist = queue.popleft()

    if curr in visited:
        continue

    visited.add(curr)
    dists[curr] = curr_dist
    
    for neighbor in connections_dict[curr]:

        if ((not neighbor in visited) and grid_dict[neighbor] != ""):
            queue.append((neighbor, curr_dist+1))
    
print(max(dists.values()))





