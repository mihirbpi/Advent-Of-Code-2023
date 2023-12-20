from aocd import get_data
import re
from collections import deque

data = get_data(year=2023, day=20)

module_type_dict = {}

for line in data.split("\n"):
    input_half, _ = line.split(" -> ")

    if (input_half == "broadcaster"):
        module_type_dict[input_half] = ["broadcaster",[]]

    else:
        module_type = input_half[0]
        module_name = input_half[1:]

        if (module_type == "%"):
            module_type_dict[module_name] = [module_type, [], "off"]

        elif (module_type == "&"):
            module_type_dict[module_name] = [module_type, [], {}]

for line in data.split("\n"):
    input_half, output_half = line.split(" -> ")
    outputs = output_half.split(", ")

    if (input_half == "broadcaster"):

        for output in outputs:
            module_type_dict[input_half][1].append(output)

            if (output in module_type_dict):

                if (module_type_dict[output][0] == "&"):
                    module_type_dict[output][2][input_half] = "low"
    else:
        module_name = input_half[1:]

        for output in outputs:
            module_type_dict[module_name][1].append(output)

            if (output in module_type_dict):

                if (module_type_dict[output][0] == "&"):
                    module_type_dict[output][2][module_name] = "low"

def run_button_push():
    Q = deque([])
    Q.append(("broadcaster",))
    low_pulses_sent = 0
    high_pulses_sent = 0

    while (len(Q) > 0):
        curr = Q.popleft()

        if (curr[0] not in module_type_dict):

            if (curr[1][1] == "low"):
                low_pulses_sent += 1
            elif (curr[1][1]) == "high":
                high_pulses_sent += 1
            continue

        if (curr[0] == "broadcaster" or curr[1][1] == "low"):
            low_pulses_sent += 1
        elif (curr[1][1] == "high"):
            high_pulses_sent += 1
        
        if (curr[0] == "broadcaster"):

            for output in module_type_dict["broadcaster"][1]:
                Q.append((output, ("broadcaster", "low")))
        elif (module_type_dict[curr[0]][0] == "%"):
            _, outputs, state =  module_type_dict[curr[0]]

            if (curr[1][1] == "high"):
                continue
            elif (state == "off"):
                module_type_dict[curr[0]][2] = "on"

                for output in outputs:
                    Q.append((output, (curr[0], "high")))
            elif (state == "on"):
                 module_type_dict[curr[0]][2] = "off"

                 for output in outputs:
                     Q.append((output, (curr[0], "low")))
        elif (module_type_dict[curr[0]][0] == "&"):
            _, outputs, memory = module_type_dict[curr[0]]
            memory[curr[1][0]] = curr[1][1]
            out = "high"

            if (all([x == "high" for x in memory.values()])):
                out = "low"

            for output in outputs:
                Q.append((output, (curr[0], out))) 
    return low_pulses_sent, high_pulses_sent

total_low_pulses = 0
total_high_pulses = 0

for i in range(1000):
    res = run_button_push()
    total_low_pulses += res[0]
    total_high_pulses += res[1]
print(total_low_pulses * total_high_pulses)