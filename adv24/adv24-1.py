from aocd import get_data
import re

data = get_data(year=2023, day=24)

hailstones = []

for line in data.split("\n"):
    pos_string, vel_string = line.split(" @ ")
    pos = tuple(map(int, pos_string.split(", ")))
    vel = tuple(map(int, vel_string.split(", ")))
    hailstones.append((pos, vel))

def det(a, b, c, d):
    return a * d - b * c

def solve_2d(a1, b1, c1, a2, b2, c2):
    D = det(a1, b1, a2, b2)
    Dx = det(c1, b1, c2, b2)
    Dy =  det(a1, c1, a2, c2)

    if (Dx != 0 and Dy != 0 and D != 0):
        return Dx / D, Dy / D
    
def find_intersection(h1, h2):
    p1, v1 = h1
    p2, v2 = h2

    res = solve_2d(v1[0], -v2[0], p2[0] - p1[0], v1[1], -v2[1] ,p2[1] - p1[1])

    if (res and res[0] >= 0 and res[1] >= 0):
        return tuple([p1[i] + res[0] * v1[i] for i in range(3)])

least = 200000000000000
most = 400000000000000
count = 0 

for i in range(len(hailstones)):

    for j in range(i, len(hailstones)):

        if (j != i):
            h1, h2 = hailstones[i], hailstones[j]
            i_res = find_intersection(h1, h2)

            if (i_res != None and (least <= i_res[0] <= most) and (least <= i_res[1] <= most)):
                count += 1

print(count)