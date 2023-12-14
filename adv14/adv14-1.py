from aocd import get_data
import re
from collections import defaultdict

data = get_data(year=2023, day=14)

round_rock_positions = []
positions = defaultdict(str)

for i in range(len(data.split("\n"))):

    for j in range(len(data.split("\n")[0])):

        if (data.split("\n")[i][j] == "O"):
            round_rock_positions.append([i,j])
        positions[(i,j)] = data.split("\n")[i][j]

round_rock_positions.sort()
curr = []

for i in range(len(round_rock_positions)):
    rock = round_rock_positions[i]
    curr = [rock[0], rock[1]]

    while ( [curr[0]-1, curr[1]] not in round_rock_positions and positions[tuple([curr[0]-1, curr[1]])] not in ["#", ""]):
        positions[tuple(curr)] = "."
        curr[0] -= 1
        round_rock_positions[i] = curr.copy()
        positions[tuple(curr)] = "O"

print(sum([len(data.split("\n")) - rock[0] for rock in round_rock_positions]))
