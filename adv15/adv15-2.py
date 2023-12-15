from aocd import get_data
import re

data = get_data(year=2023, day=15)
steps = data.strip().split(",")

def hash(s):
    curr = 0

    for c in s:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr

boxes = [[] for i in range(256)]

for step in steps:

    if ("-" in step):
        label = step.split("-")[0]
        box = boxes[hash(label)]

        for i in range(len(box)):

            if (box[i][0] == label):
                box.pop(i)
                break

    elif ("=" in step):
        label = step.split("=")[0]
        focal_length = int(step.split("=")[1])
        box = boxes[hash(label)]
        lens_exists = False

        for i in range(len(box)):

            if (box[i][0] == label):
                box[i] = [label, focal_length]
                lens_exists = True
                break

        if (not lens_exists):
            box.append([label, focal_length])

answer = 0

for box_no in range(len(boxes)):
    box = boxes[box_no]

    for lens_idx in range(len(box)):
        answer += (box_no+1)*(lens_idx+1)*box[lens_idx][1]
        
print(answer)
