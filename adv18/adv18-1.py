from aocd import get_data
import re

data = get_data(year=2023, day=18)

dir_dict = {"R": (0,1), "L": (0,-1), "D": (1,0), "U": (-1,0)}
curr_i = 0
curr_j = 0
boundary = []
b = 0

for line in data.split("\n"):
    dir, amount, _ = re.split('\s+', line)
    curr_i += dir_dict[dir][0] * int(amount)
    curr_j += dir_dict[dir][1] * int(amount)
    b += int(amount)
    boundary.append((curr_i, curr_j))

area = 0

for i in range(len(boundary)):
    x1, y1 = boundary[i]
    x2, y2 = boundary[(i+1) % len(boundary)]
    area += (x1*y2 - x2*y1)
area /= 2
area = abs(area)
# i = A - b/2 + 1 (pick's theorem)
interior = int(area - b/2 + 1)
print(interior + b)



    
