from aocd import get_data

data = get_data(year=2023, day=2)
games  = data.split("\n")

num_cubes_dict = {"red": 12, "green": 13, "blue": 14}
possible_count = 0

for id in range(len(games)):
    game = games[id]
    possible = True

    for set in  game.split(": ")[1].split("; "):

        for color_data in set.split(", "):
            count, color_name = color_data.split(" ")

            if (int(count) > num_cubes_dict[color_name]):
                possible = False

    possible_count += (1 + id if possible else 0)
    
print(possible_count)



