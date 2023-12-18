from aocd import get_data
import re

data = get_data(year=2023, day=18)

dir_dict = {"0": (0,1), "1": (1,0), "2": (0,-1), "3": (-1,0)}
curr_i = 0
curr_j = 0
boundary = []
b = 0

for line in data.split("\n"):
    _, _, hex = re.split('\s+', line)
    amount  = int(hex[2:-2],16)
    curr_i += dir_dict[hex[-2]][0] * amount
    curr_j += dir_dict[hex[-2]][1] * amount
    b += amount
    boundary.append((curr_i,curr_j))

area = 0

for i in range(len(boundary)):
    x1, y1 = boundary[i]
    x2, y2 = boundary[(i+1) % len(boundary)]
    area += (x1*y2 - x2*y1) / 2
area = abs(area)
# i = A - b/2 + 1 (pick's theorem)
interior = int(area - b/2 + 1)
print(interior + b)



    
