from aocd import get_data
import re
import itertools

data = get_data(year=2023, day=12)

answer = 0

for line in data.split("\n"):
    pattern, condition = line.split(" ")
    condition = list(map(int, condition.split(",")))

    re_string = r"(\.*)"

    for num in condition[:-1]:
        re_string += "#{"+str(num)+"}(\.+)"
    re_string += "#{"+str(condition[-1])+"}(\.*)"
    question_indices = []

    for i in range(len(pattern)):

        if (pattern[i] == "?"):
            question_indices.append(i)

    N = len(question_indices)
    perms = itertools.chain((N*(0,),), (l[0] * (0,) + sum(((1,) + (i-j-1) * (0,) for i, j in zip(l[1:], l[:-1])), ()) + (1,) + (N-l[-1]-1)*(0,) for k in range(1,N+1) for l in itertools.combinations(range(N), k)))
    pattern_as_list = list(pattern)

    for p in perms:
        p_pattern_as_list = pattern_as_list.copy()

        for i in range(len(question_indices)):

            if (p[i] == 0):
                p_pattern_as_list[question_indices[i]] = "#"
            else:
                p_pattern_as_list[question_indices[i]] = "."

        p_pattern_as_string = "".join(p_pattern_as_list)

        if(re.fullmatch(re_string, p_pattern_as_string) != None):
            answer += 1
print(answer)
    


