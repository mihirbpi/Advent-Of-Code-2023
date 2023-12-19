from aocd import get_data
import re
from copy import deepcopy

data = get_data(year=2023, day=19)

workflow_lines = data.split("\n\n")[0].split("\n")
workflow_dict = {}

for line in workflow_lines:
    workflow_name = line.split("{")[0]
    rules = line.split("{")[1].strip("}").split(",")
    workflow_dict[workflow_name] = rules

def num_accepted(ranges_list, workflow_name):

    if (workflow_name == "R"):
        return 0
    
    if (workflow_name == "A"):
        res = 1

        for r in ranges_list:
            res *= (r[1]-r[0]+1)
        return res
    
    total = 0
    rules = workflow_dict[workflow_name]

    for rule in rules[:-1]:
        condition, destination = rule.split(":")
        letter_index = ["x","m","a","s"].index(condition[0])
        sign = condition[1]
        value = int(condition[2:])

        if (sign == "<"):
            old_low, old_high = ranges_list[letter_index]
            true_low, true_high = max(1,old_low), min(value-1, old_high)
            false_low, false_high = max(value, old_low), min(4000, old_high)

        elif (sign == ">"):
            old_low, old_high = ranges_list[letter_index]
            true_low, true_high = max(value + 1, old_low), min(4000,old_high)
            false_low, false_high = max(1,old_low), min(value,old_high)

        if (true_low <= true_high):
            new_ranges_list = deepcopy(ranges_list)
            new_ranges_list[letter_index] = (true_low, true_high)
            total += num_accepted(new_ranges_list, destination)

        if (false_low <= false_high):
            ranges_list[letter_index] = (false_low, false_high)

    total += num_accepted(ranges_list, rules[-1])
    return total


print(num_accepted([[1,4000], [1,4000], [1,4000], [1,4000]], "in"))