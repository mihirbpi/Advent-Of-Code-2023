from aocd import get_data
import re
from collections import deque

data = get_data(year=2023, day=16)

dir_to_vector = {"R": [0,1], "L": [0,-1], "U": [-1,0], "D": [1,0]}
dir_mirror = {"R": {"/": "U", "\\": "D"}, "L": {"/": "D", "\\": "U"}, "U": {"/": "R", "\\": "L"}, "D": {"/": "L", "\\": "R"} }
dir_splitter = {"R": {"|": "UD"}, "L": {"|": "UD"}, "U": {"-": "LR"}, "D": {"-": "LR"}    }

m = len(data.split("\n"))
n = len(data.split("\n")[0])
grid = data.split("\n")
beams = deque([ ((0,-1),"R") ])
visited = set()

while(len(beams) > 0):
    beam = beams.popleft()
    new_pos = (beam[0][0] + dir_to_vector[beam[1]][0], beam[0][1] + dir_to_vector[beam[1]][1])

    if (new_pos[0] not in range(m) or new_pos[1] not in range(n)):
          continue
    entity = grid[new_pos[0]][new_pos[1]]

    if (entity in "/\\"):
        to_add = ((new_pos, dir_mirror[beam[1]][entity]))

        if (to_add not in visited):
              visited.add(to_add)
              beams.append(to_add)

    elif entity in "-|" and entity in dir_splitter[beam[1]]:
        to_add1 = (new_pos, dir_splitter[beam[1]][entity][0])
        to_add2 = (new_pos, dir_splitter[beam[1]][entity][1])

        if (to_add1 not in visited):
              visited.add(to_add1)
              beams.append(to_add1)
              to_continue = True

        if (to_add2 not in visited):
             visited.add(to_add)
             beams.append(to_add2)
    else:
     to_add = (new_pos, beam[1])

     if (to_add not in visited):
            visited.add(to_add)
            beams.append(to_add)

print(len(set([x[0] for x in  visited])))      
         


