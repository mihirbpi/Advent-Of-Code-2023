from aocd import get_data
import re

data = get_data(year=2023, day=13)
patterns = data.split("\n\n")

def is_horiz_smudge_reflection(lines, i):
    smudge_count = 0

    if (i == len(lines)-1):
        return False
    
    for j in range(i+1, len(lines)):
        
        if (i - (j - (i+1)) > -1):
            r1 = lines[j]
            r2 = lines[i - (j - (i+1))]
            smudge_count += sum([r1[k] != r2[k] for k in range(len(r1))])

    if (smudge_count == 1):
        return True

    for j in range(i+1): 
        
        if (i+1 + i-j < len(lines)):
            r1 = lines[j]
            r2 = lines[i - (j - (i+1))]
            smudge_count += sum([r1[k] != r2[k] for k in range(len(r1))])

    return smudge_count == 1

def is_vert_smudge_reflection(lines, i):

    smudge_count = 0

    cols = [ [line[j] for line in lines] for j in range(len(lines[0]))]

    if (i == len(cols)-1):
        return False
    
    for j in range(i+1, len(cols)):
        
        if (i - (j - (i+1)) > -1):
            c1 = cols[j]
            c2 = cols[i - (j - (i+1))]
            smudge_count += sum([c1[k] != c2[k] for k in range(len(c1))])

    if (smudge_count == 1):
        return True
    
    for j in range(i+1):

        if (i+1 + i-j < len(cols)):
            c1 = cols[j]
            c2 = cols[i+1 + i-j]
            smudge_count += sum([c1[k] != c2[k] for k in range(len(c1))])

    return smudge_count == 1

answer = 0

for pattern in patterns:
    found_reflection = False
    lines = pattern.split("\n")

    for j in range(len(lines[0])):

        if (is_vert_smudge_reflection(lines,j)):
            answer += j+1  
            break

    for i in range(len(lines)):

        if(is_horiz_smudge_reflection(lines,i)):
            answer += 100*(i+1)
            break

print(answer)
