from aocd import get_data
import re
from collections import deque

data = get_data(year=2023, day=22)

bricks = []

for line in data.split("\n"):
    bricks.append([list(map(int,x.split(","))) for x in line.split("~")])


def overlap(brick1, brick2):
    x_overlap_left = max(brick1[0][0], brick2[0][0])
    x_overlap_right = min(brick1[1][0], brick2[1][0])
    y_overlap_left = max(brick1[0][1], brick2[0][1])
    y_overlap_right = min(brick1[1][1], brick2[1][1])

    return x_overlap_left <= x_overlap_right and y_overlap_left <= y_overlap_right

bricks.sort(key=lambda x: max(x[0][2], x[1][2]))

for i in range(len(bricks)):
    height = 1
    curr_brick = bricks[i]
    bricks_to_check = bricks[:i]

    for other_brick in bricks_to_check:
                                  
        if (overlap(curr_brick, other_brick)):
            height = max(height, 1 + other_brick[1][2])
    curr_brick[1][2] = curr_brick[1][2] - (curr_brick[0][2] - height) 
    curr_brick[0][2] = height
      
bricks.sort(key=lambda x: max(x[0][2], x[1][2]))
bricks_supported = {i: set() for i in range(len(bricks))}
supporting_bricks = {i: set() for i in range(len(bricks))} 

for i in range(len(bricks)):

    for j in range(i):

        if (overlap(bricks[i], bricks[j]) and bricks[i][0][2] == 1 + bricks[j][1][2]):
            supporting_bricks[i].add(j)
            bricks_supported[j].add(i)

answer = 0

for i in range(len(bricks)):
    queue = deque([j for j in bricks_supported[i] if len(supporting_bricks[j])< 2])
    falling = set(queue)
    falling.add(i)

    while(queue):
        j = queue.popleft()

        for k in bricks_supported[j] - falling:

            if (supporting_bricks[k] <= falling):
                queue.append(k)
                falling.add(k)

    answer += len(falling) - 1

print(answer)