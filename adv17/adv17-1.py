from aocd import get_data
import re
from heapq import heappop, heappush

data = get_data(year=2023, day=17)

grid = [list(map(int, line)) for line in  data.split("\n")]
priority_q = [(0,0,0,0,0,0)]
seen = set()

while(len(priority_q) > 0):
    heat_loss, r, c, dr, dc, steps = heappop(priority_q) 

    if ((r, c, dr, dc, steps) not in seen and r in range(len(grid)) and c in range(len(grid[0]))):
        seen.add((r, c, dr, dc, steps) )

        if ((r,c) == (len(grid)-1, len(grid[0])-1)):
            print(heat_loss)
            break

        if (steps < 3 and (dr,dc) != (0,0)):
            nr = r + dr
            nc = c + dc

            if (nr in range(len(grid)) and nc in range(len(grid[0]))):
                heappush(priority_q, (heat_loss + grid[nr][nc], nr, nc, dr, dc, steps + 1))

        for ndr, ndc in [(0,1), (0,-1), (1,0), (-1,0)]:

            if ((ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc)):
                 nr = r+ndr
                 nc = c+ndc
                 
                 if (nr in range(len(grid)) and nc in range(len(grid[0]))):
                    heappush(priority_q, (heat_loss + grid[nr][nc], nr, nc, ndr, ndc, 1))
        

