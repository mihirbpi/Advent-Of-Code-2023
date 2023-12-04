from aocd import get_data
from collections import defaultdict

data = get_data(year=2023, day=3)
rows = data.split("\n")

grid = defaultdict(lambda : ".")

for i in range(len(rows)):

    for j in range(len(rows[0])):
        grid[(i,j)] = rows[i][j]

number_list = []

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
                number_list.append((int(number), tuple(num_positions)))
            number = ""
            num_positions = []
            j += 1
answer = 0

for entry in number_list:
    num_positions = entry[1]
    part = False

    for i,j in num_positions:

        for dir in [[-1,1], [-1,0], [-1,-1], [0,1], [0,-1], [1,1], [1,0], [1,-1]]:

            if grid[(i+dir[0], j+dir[1])] not in ".0123456789":
                part = True
                break

        if (part):
            break

    if (part):
        answer += entry[0]
print(answer)


            

            

