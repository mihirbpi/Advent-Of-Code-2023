from aocd import get_data
from collections import defaultdict
import numpy as np

data = get_data(year=2023, day=3)
rows = data.split("\n")

grid = defaultdict(lambda : ".")

for i in range(len(rows)):

    for j in range(len(rows[0])):
        grid[(i,j)] = rows[i][j]

number_dict = {}

for i in range(len(rows)):
    number = ""
    num_positions = []
    j = 0

    while (j < len(rows[0]) + 1 ):
        
        if (j < len(rows[0]) and grid[(i,j)] in "0123456789"):
            number += grid[(i,j)]
            num_positions.append((i,j))
            j += 1
        else:

            if (number != "" and len(num_positions) > 0):

                for pos in num_positions:
                    number_dict[pos] = int(number)
            number = ""
            num_positions = []
            j += 1

answer = 0

for i, j in grid:
    numbers_around = set()

    if (grid[(i,j)] == "*"):

        for dir in [[-1,1], [-1,0], [-1,-1], [0,1], [0,-1], [1,1], [1,0], [1,-1]]:
            x, y = (i+dir[0], j+dir[1])

            if grid[(x, y)] in "0123456789":
                    numbers_around.add(number_dict[(x,y)])
                    
            if(len(numbers_around) == 2):
                answer += np.prod(list(numbers_around))
                break
print(answer)


            

            

