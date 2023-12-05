from aocd import get_data
import re

data = get_data(year=2023, day=5)
seeds_string = data.split("\n\n")[0]
maps_strings = data.split("\n\n")[1:]
seeds_info = list(map(int, re.split('\s+', seeds_string)[1:]))
seed_intervals = []

for i in range(0,len(seeds_info)-1,2):
    start, length  = seeds_info[i:i+2]
    seed_intervals.append((start, start+length))

resource_maps = []

for m_string in maps_strings:
    mappings = m_string.split("\n")[1:]
    resource_submaps = []

    for mapping in mappings:
        dest, source, length = list(map(int, re.split('\s+', mapping)))
        resource_submaps.append((dest, source, length))
    resource_maps.append(resource_submaps)

curr_intervals = seed_intervals

for resource_map in resource_maps:
    new_intervals = []

    while (len(curr_intervals) > 0):
        s, e = curr_intervals.pop()
        found = False
        
        for dest, source, length in resource_map:
            os = max(s, source)
            oe = min(e, source + length)

            if (os < oe):
                new_intervals.append((dest + os - source, dest + oe - source))

                if (os > s):
                    curr_intervals.append((s, os))

                if (oe < e):
                    curr_intervals.append((oe, e))
                found = True
                break

        if (not found):
            new_intervals.append((s, e))

    curr_intervals = new_intervals

print(min(curr_intervals)[0])
