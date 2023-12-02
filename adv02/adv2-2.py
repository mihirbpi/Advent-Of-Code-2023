from aocd import get_data
import numpy as np
data = get_data(year=2023, day=2)
games  = data.split("\n")

power_count = 0

for id in range(len(games)):
    game = games[id]
    possible = True
    fewest_cubes_dict = {"red": 0 , "green": 0, "blue": 0}

    for set in  game.split(": ")[1].split("; "):

        for color_data in set.split(", "):
            count, color_name = color_data.split(" ")
            fewest_cubes_dict[color_name] = max(fewest_cubes_dict[color_name], int(count))
    power = np.prod(list(fewest_cubes_dict.values()))
    power_count += power

print(power_count)



