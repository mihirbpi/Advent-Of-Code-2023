from aocd import get_data
import re
from collections import defaultdict
from copy import deepcopy

data = get_data(year=2023, day=14)

grid = [[data.split("\n")[i][j] for j in range(len(data.split("\n")[0]))] for i in range(len(data.split("\n")))]

def slide_north(grid):
    round_rock_positions = []

    for i in range(len(grid)):

        for j in range(len(grid[0])):

            if (grid[i][j] == "O"):
                round_rock_positions.append([i,j])

    round_rock_positions.sort()
    curr = []

    for i in range(len(round_rock_positions)):
        rock = round_rock_positions[i]
        curr = [rock[0], rock[1]]

        while ( [curr[0]-1, curr[1]] not in round_rock_positions and grid[curr[0]-1][curr[1]] != "#" and curr[0]-1 >= 0):
            grid[curr[0]][curr[1]] = "."
            curr[0] -= 1
            round_rock_positions[i] = curr.copy()
            grid[curr[0]][curr[1]] = "O"

def rotate_90_clock(grid):
    new_grid = [ [grid[i][j] for i in range(len(grid)-1,-1,-1)] for j in range(len(grid[0]))]
    return new_grid

def rotate_90_counterclock(grid):
    new_grid = deepcopy(grid)

    for i in range(3):
        new_grid = rotate_90_clock(new_grid)

    return new_grid

def do_cycle(grid):
    # north
    slide_north(grid)
    # west
    new_grid = rotate_90_clock(grid)
    slide_north(new_grid)
    new_grid = rotate_90_counterclock(new_grid)
    # south
    new_grid = rotate_90_clock(new_grid)
    new_grid = rotate_90_clock(new_grid)
    slide_north(new_grid)
    new_grid = rotate_90_counterclock(new_grid)
    new_grid = rotate_90_counterclock(new_grid)  
    # east
    new_grid = rotate_90_counterclock(new_grid)
    slide_north(new_grid)
    new_grid = rotate_90_clock(new_grid)
    return new_grid

def calculate_load(grid):
    round_rock_positions = []
    for i in range(len(grid)):

        for j in range(len(grid[0])):

            if (grid[i][j] == "O"):
                round_rock_positions.append([i,j])

    return sum([len(grid) - rock[0] for rock in round_rock_positions])

cycle_no_to_grid = {}
last_seen_grid = {}

for cycle in range(1,10**9+1):
    grid = do_cycle(grid)
    grid_hash = "\n".join(["".join(grid[i]) for i in range(len(grid))])
    
    if (grid_hash in last_seen_grid):
        last_seen_cycle = last_seen_grid[grid_hash]
        period = cycle - last_seen_cycle
        grid = cycle_no_to_grid[last_seen_cycle + ((10**9-last_seen_cycle) % period) ]
        answer = calculate_load(grid)
        break

    cycle_no_to_grid[cycle] = deepcopy(grid)
    last_seen_grid[grid_hash] = cycle

print(answer)