from aocd import get_data

data = get_data(year=2023, day=12)

def num_ways(pattern, condition, cache):
    if (pattern == ""):
        return 1 if condition == () else 0

    if (condition == ()):
        return 1 if "#" not in pattern else 0

    if ((pattern, condition) in cache):
        return cache[(pattern, condition)]

    res = 0

    if (pattern[0] in ".?"):
        res += num_ways(pattern[1:], condition, cache)
    
    if (pattern[0] in "#?"):
        if (condition[0] <= len(pattern) and "." not in pattern[:condition[0]] and (condition[0] == len(pattern) or pattern[condition[0]] != "#" )):
            res += num_ways(pattern[condition[0]+1:], condition[1:], cache)
    cache[(pattern, condition)] = res
    return res

answer = 0

for line in data.split("\n"):
    cache = {}
    pattern, condition = line.split(" ")
    pattern = "?".join([pattern]*5)
    condition = tuple(map(int, condition.split(",")*5))
    answer += num_ways(pattern, condition, cache)
print(answer)
    


