from aocd import get_data
import re

data = get_data(year=2023, day=5)

seeds_string = data.split("\n\n")[0]
maps_strings = data.split("\n\n")[1:]
seeds = list(map(int, re.split('\s+', seeds_string)[1:]))
resource_maps = []

for m_string in maps_strings:
    mappings = m_string.split("\n")[1:]
    resource_submaps = []

    for mapping in mappings:
        dest, source, length = list(map(int, re.split('\s+', mapping)))
        resource_submaps.append([dest, source, length])
    resource_maps.append(resource_submaps)

answer = 1e100

for seed in seeds:
    location = seed

    for i in range(len(resource_maps)):
        resource_map = resource_maps[i]

        for submap in resource_map:
            dest, source, length = submap
            diff = location - source

            if (diff < length and diff >= 0):
                location = dest + diff
                break
            else:
                continue

    answer = min(answer, location)

print(answer)