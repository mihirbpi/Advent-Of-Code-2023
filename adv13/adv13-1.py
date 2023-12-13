from aocd import get_data
import re

data = get_data(year=2023, day=13)
patterns = data.split("\n\n")

def is_horiz_reflection(lines, i):
    
    if (i == len(lines)-1):
        return False
    
    for j in range(i+1, len(lines)):

        if (i - (j - (i+1)) > -1):

            if (lines[j] != lines[i - (j - (i+1))]):
                return False
            
    for j in range(i+1):

        if (i+1 + i-j < len(lines)):

            if (lines[j] != lines[i+1 + i-j]):
                return False
    return True

def is_vert_reflection(lines, i):

    cols = [ [line[j] for line in lines] for j in range(len(lines[0]))]

    if (i == len(cols)-1):
        return False
    
    for j in range(i+1, len(cols)):

        if (i - (j - (i+1)) > -1):

            if (cols[j] != cols[i - (j - (i+1))]):
                return False
            
    for j in range(i+1):

        if (i+1 + i-j < len(cols)):

            if (cols[j] != cols[i+1 + i-j]):
                return False
    return True

answer = 0

for pattern in patterns:
    found_reflection = False
    lines = pattern.split("\n")

    for j in range(len(lines[0])):

        if (is_vert_reflection(lines,j)):
            answer += j+1  
            break

    for i in range(len(lines)):

        if(is_horiz_reflection(lines,i)):
            answer += 100*(i+1)
            break

print(answer)
