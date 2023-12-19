from aocd import get_data
import re

data = get_data(year=2023, day=19)

workflow_lines = data.split("\n\n")[0].split("\n")
part_lines = data.split("\n\n")[1].split("\n")
workflow_dict = {}

for line in workflow_lines:
    workflow_name = line.split("{")[0]
    rules = line.split("{")[1].strip("}").split(",")
    workflow_dict[workflow_name] = rules

parts = []

for line in part_lines:
    parts.append([int(x.split("=")[1]) for x in line[1:-1].split(",")])

def get_result(part):
    curr_workflow_name = "in"

    while (True):

        if (curr_workflow_name == "A"):
            return True
        
        elif (curr_workflow_name == "R"):
            return False
        curr_workflow = workflow_dict[curr_workflow_name]

        for rule in curr_workflow:

            if ":" in rule:
                condition, destination = rule.split(":")
                letter_index = ["x","m","a","s"].index(condition[0])
                sign = condition[1]
                value = int(condition[2:])

                if (sign == "<" and part[letter_index] < value):
                    curr_workflow_name = destination
                    break
                
                elif (sign == ">" and part[letter_index] > value):
                    curr_workflow_name = destination
                    break
            else:
                curr_workflow_name = rule

print(sum([sum(part) for part in parts if get_result(part)]))