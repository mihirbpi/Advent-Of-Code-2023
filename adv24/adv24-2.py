from aocd import get_data
import re
import sympy

data = get_data(year=2023, day=24)

hailstones = []

ps1, ps2, ps3, vs1, vs2, vs3 = sympy.symbols("ps1, ps2, ps3, vs1, vs2, vs3")

for line in data.split("\n"):
    pos_string, vel_string = line.split(" @ ")
    pos = tuple(map(int, pos_string.split(", ")))
    vel = tuple(map(int, vel_string.split(", ")))
    hailstones.append((pos, vel))

equations = []

for i in range(3):
    (p1, p2, p3), (v1, v2, v3) = hailstones[i]
    equations.append(sympy.Eq( (p1 - ps1) * (vs2 - v2), (p2 - ps2) * (vs1 - v1)))
    equations.append(sympy.Eq((p2 - ps2) * (vs3 - v3), (p3 - ps3) * (vs2 - v2)))

answers = sympy.solve(equations)
print(sum([answers[0][x] for x in [ps1, ps2, ps3]]))