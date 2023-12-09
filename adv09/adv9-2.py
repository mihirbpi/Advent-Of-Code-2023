from aocd import get_data
import re

data = get_data(year=2023, day=9)

sequences = []

for line in data.split("\n"):
    sequences.append(list(map(int, re.split('\s+', line))))

def get_difference_seqs(seq):
    curr = seq.copy()
    res = [curr]

    while(curr != [0]*len(curr)):
        new = []

        for i in range(len(curr)-1):
            new.append(curr[i+1] - curr[i])

        res.append(new)
        curr = new

    return res

def predict_next(seq):
    diff_seqs = get_difference_seqs(seq)

    for i in range(len(diff_seqs)-2,-1,-1):
        diff_seqs[i].append(diff_seqs[i+1][-1] + diff_seqs[i][-1])

    return diff_seqs[0][-1]
    
print(sum([predict_next(list(reversed(seq))) for seq in sequences]))