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

answer = sum([hash(step) for step in steps])
print(answer)
