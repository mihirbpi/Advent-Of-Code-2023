from aocd import get_data
import re
from collections import deque

data = get_data(year=2023, day=21)
grid = data.split("\n")
grid_dict = {}
start = None

for i in range(len(grid)):

    for j in range(len(grid[0])):
        grid_dict[(i,j)] = grid[i][j]
        
        if (grid[i][j] == "S"):
            start = (i,j)

def fill(s, num_steps):
    queue = deque([(s, num_steps)])
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

    return(len(answer))

assert len(grid) == len(grid[0])
size = len(grid)
assert start[0] == start[1] == size // 2
steps = 26501365
assert steps % size == size // 2

grid_width = steps // size - 1

odd = (grid_width // 2 * 2 + 1) ** 2
even = ((grid_width + 1) // 2 * 2) ** 2

odd_points = fill(start, size * 2 + 1)
even_points = fill(start, size * 2)

corner_t = fill((size - 1, start[1]), size - 1)
corner_r = fill((start[0], 0), size - 1)
corner_b = fill((0, start[1]), size - 1)
corner_l = fill((start[0], size - 1), size - 1)

small_tr = fill((size - 1, 0), size // 2 - 1)
small_tl = fill((size - 1, size - 1), size // 2 - 1)
small_br = fill((0, 0), size // 2 - 1)
small_bl = fill((0, size - 1), size // 2 - 1)

large_tr = fill((size - 1, 0), size * 3 // 2 - 1)
large_tl = fill((size - 1, size - 1), size * 3 // 2 - 1)
large_br = fill((0, 0), size * 3 // 2 - 1)
large_bl = fill((0, size - 1), size * 3 // 2 - 1)

print (
    odd * odd_points +
    even * even_points +
    corner_t + corner_r + corner_b + corner_l +
    (grid_width + 1) * (small_tr + small_tl + small_br + small_bl) + 
    grid_width * (large_tr + large_tl + large_br + large_bl)
)