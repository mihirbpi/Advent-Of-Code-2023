from aocd import get_data
import re
from collections import defaultdict, deque

data = get_data(year=2023, day=21)
grid = data.split("\n")
grid_dict = {}
start = None

for i in range(len(grid)):

    for j in range(len(grid[0])):
        grid_dict[(i,j)] = grid[i][j]

        if (grid[i][j] == "S"):
            start = (i,j)

num_steps = 64
queue = deque([(start, num_steps)])
answer = set()
visited = set()

while (len(queue) > 0):
    curr_pos, depth = queue.popleft()

    if(curr_pos in visited):
         continue

    if (depth == 0):
        answer.add(curr_pos)
        continue

    if (depth % 2 == 0):
        answer.add(curr_pos)
    
    visited.add(curr_pos)

    for dir in [(0,1), (0,-1), (1,0), (-1,0)]:

        new_pos = (curr_pos[0]+dir[0], curr_pos[1]+dir[1])

        if (new_pos in grid_dict and grid_dict[new_pos] in ".S" and new_pos not in visited):
                queue.append((new_pos, depth-1))

print(len(answer))