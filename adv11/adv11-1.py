from aocd import get_data
import re

data = get_data(year=2023, day=11)

def row_contains_galaxies(row):
    return all([x == "." for x in row])

def col_contains_galaxies(col):
    return all([x == "." for x in col])

galaxy_positions = []
empty_cols = set()
empty_rows = set()
expansion = 2

for i in range(len(data.split("\n"))):

    for j in range(len(data.split("\n")[0])):

        if(row_contains_galaxies(data.split("\n")[i])):
            empty_rows.add(i)

        if(col_contains_galaxies([x[j] for x in data.split("\n")])):
            empty_cols.add(j)

        if(data.split("\n")[i][j] == "#"):
            galaxy_positions.append((i,j))
answer = 0

for i in range(len(galaxy_positions)):
    r1, c1 = galaxy_positions[i]

    for r2, c2 in galaxy_positions[:i]:

        for r in range(min(r1,r2),max(r1,r2)):
            answer += expansion if r in empty_rows else 1

        for c in range(min(c1,c2),max(c1,c2)):
            answer += expansion if c in empty_cols else 1
            
print(answer)






