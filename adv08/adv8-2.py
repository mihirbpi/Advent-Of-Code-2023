from aocd import get_data
import math
import re

data = get_data(year=2023, day=8)

dir_string = data.split("\n\n")[0]
node_defs = data.split("\n\n")[1].split("\n")
node_defs_dict = {}

for node_def in node_defs:
    x = re.findall(r'(\w+) = \((\w+), (\w+)\)', node_def)
    node_defs_dict[x[0][0]] = (x[0][1], x[0][2])

def get_length_to_z(start):
    curr_elem = start
    steps_to_reach = 0
    curr_index = 0

    while(True):
        curr_dir = dir_string[curr_index % len(dir_string)]
        curr_elem = node_defs_dict[curr_elem][['L', 'R'].index(curr_dir)]
        curr_index += 1
        steps_to_reach += 1

        if(curr_elem[-1] == 'Z'):
            break

    return steps_to_reach

lengths_list = []

for node in node_defs_dict:

    if(node[-1] == 'A'):
        lengths_list.append(get_length_to_z(node))

answer = math.lcm(*lengths_list)
print(answer)